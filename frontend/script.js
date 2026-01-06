const dropArea = document.getElementById("drop-area");
const input = document.getElementById("audioInput");
const fileNameDisplay = document.getElementById("fileName");
const loader = document.getElementById("loader");
const resultBox = document.getElementById("resultBox");
const genreText = document.getElementById("genreText");
const confidenceText = document.getElementById("confidenceText");
const confidenceFill = document.getElementById("confidenceFill");

// Click to Upload
dropArea.addEventListener("click", () => input.click());

input.addEventListener("change", function () {
  if (this.files && this.files[0]) {
    fileNameDisplay.innerText = "Selected: " + this.files[0].name;
  }
});

// Drag & Drop Effects
dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.classList.add("highlight-drag");
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("highlight-drag");
});

dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  dropArea.classList.remove("highlight-drag");
  if (e.dataTransfer.files.length) {
    input.files = e.dataTransfer.files;
    fileNameDisplay.innerText = "Selected: " + input.files[0].name;
  }
});

// Predict Function
async function predictGenre() {
  if (input.files.length === 0) {
    alert("Please select an audio file first!");
    return;
  }

  // UI Updates
  resultBox.style.display = "none";
  loader.style.display = "flex";

  const formData = new FormData();
  formData.append("file", input.files[0]);

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    loader.style.display = "none";

    if (data.error) {
      alert("Error: " + data.error);
    } else {
      // Show Result
      resultBox.style.display = "block";
      genreText.innerText = data.genre.toUpperCase();
      confidenceText.innerText = "Confidence: " + data.confidence;

      // Animate Bar
      let confValue = parseFloat(data.confidence);
      setTimeout(() => {
        confidenceFill.style.width = confValue + "%";
      }, 100);
    }
  } catch (error) {
    loader.style.display = "none";
    alert("Cannot connect to Backend server!");
  }
}
