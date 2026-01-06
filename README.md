# 🎵 Music Genre Classification

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

**SonicSense AI** is an end-to-end Deep Learning application that classifies audio tracks into musical genres (e.g., Rock, Jazz, Hip-Hop, Classical) using **Convolutional Neural Networks (CNN)** and **Mel Spectrograms**.

The project includes a complete pipeline: **Data Processing -> Model Training -> Backend API -> Modern Frontend UI**.

---

## 📸 Project Demo

<img width="1864" height="842" alt="image" src="https://github.com/user-attachments/assets/f778ad83-17ce-4962-bfd8-3345d4c1a98c" />
<img width="1498" height="841" alt="image" src="https://github.com/user-attachments/assets/58100ad4-29c2-40df-9203-05139b71d221" />



## 🌟 Features

* **Advanced Audio Processing:** Converts raw audio into Mel Spectrograms using `librosa`.
* **Deep Learning Model:** Custom CNN architecture trained on the **GTZAN Dataset**.
* **FastAPI Backend:** High-performance API to handle predictions.
* **Modern Frontend:** Responsive HTML/CSS UI with Drag & Drop support and visual animations.
* **Real-time Analysis:** Processes audio chunks and predicts genres with confidence scores.

---

## 📂 Project Structure

```bash
Music-Genre-AI-Project/
│
├── 📜 music_genre_solution.ipynb   # Jupyter Notebook (Training Logic)
├── 📜 requirements.txt             # Python Dependencies
│
├── 📂 backend/                     # FastAPI Server
│   ├── main.py                     # API Logic
│   └── model/                      # Place your trained .keras model here
│
└── 📂 frontend/                    # User Interface
    ├── index.html                  # Main UI
    ├── style.css                   # Glassmorphism Styling
    └── script.js                   # Frontend Logic

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/Music-Genre-AI-Project.git](https://github.com/YOUR_USERNAME/Music-Genre-AI-Project.git)
cd Music-Genre-AI-Project

```

### 2. Install Dependencies

Make sure you have Python installed.

```bash
pip install -r requirements.txt

```

### 3. Train the Model (Important!)

*Since the trained model is too large for GitHub, you need to generate it first.*

1. Open `music_genre_solution.ipynb`.
2. Run all cells to train the CNN.
3. The notebook will save a file named **`music_genre_cnn.keras`**.
4. Move this file into the `backend/model/` folder.

### 4. Start the Backend Server

Navigate to the backend folder and run the server:

```bash
cd backend
python -m uvicorn main:app --reload

```

*You should see: `✅ Model loaded successfully!*`

### 5. Launch the App

* Go to the `frontend` folder.
* Open **`index.html`** in your browser (Chrome/Edge).
* Drag and drop an audio file to see the magic! 🎧

---

## 📊 Dataset

This model is trained on the **GTZAN Genre Collection**, which consists of 1,000 audio tracks each 30 seconds long. It contains 10 genres:

* Blues, Classical, Country, Disco, Hiphop, Jazz, Metal, Pop, Reggae, Rock.

---

## 🛠️ Tech Stack

* **Language:** Python
* **ML/DL:** TensorFlow, Keras, Librosa, NumPy, Scikit-learn
* **Backend:** FastAPI, Uvicorn
* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (Fetch API)

---

### 👨‍💻 Author

Developed by **Harsh Porwal** 

```
