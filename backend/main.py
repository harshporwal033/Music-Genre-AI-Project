from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
import librosa
import os
import shutil

app = FastAPI()

# Frontend ko allow karne ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model Load karna
MODEL_PATH = "../model/music_genre_cnn.keras"
print(f"Loading model from: {MODEL_PATH}")

try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    print("✅ Model loaded successfully!")
except Exception as e:
    model = None
    print(f"⚠️ Error loading model: {e}")

GENRES = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

def preprocess_audio(file_path):
    # Audio Processing Logic
    SAMPLE_RATE = 22050
    DURATION = 3 
    y, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
    
    expected_samples = SAMPLE_RATE * DURATION
    if len(y) < expected_samples:
        y = np.pad(y, (0, int(expected_samples - len(y))), mode='constant')
        
    melspec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, n_fft=2048, hop_length=512)
    melspec_db = librosa.power_to_db(melspec, ref=np.max)
    
    target_width = 130
    if melspec_db.shape[1] > target_width:
        melspec_db = melspec_db[:, :target_width]
    else:
        melspec_db = np.pad(melspec_db, ((0,0), (0, target_width - melspec_db.shape[1])))
    
    return melspec_db.reshape(1, 128, 130, 1)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if model is None:
        return {"error": "Model not loaded"}
    
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        processed_data = preprocess_audio(temp_filename)
        prediction = model.predict(processed_data)
        class_idx = np.argmax(prediction)
        confidence = float(np.max(prediction))
        
        return {"genre": GENRES[class_idx], "confidence": f"{confidence * 100:.2f}%"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)