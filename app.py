from flask import Flask, render_template, request
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
import os
import time

app = Flask(__name__)

# Ensure upload folder exists
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load CLIP (VLM)
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# PROMPTS (this is your "classification logic")
labels = [
    "a large agricultural farmland with organized crop rows and farming activity",
    "a non agricultural scene like buildings roads people indoor or wild forest"
]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    image_path = None

    if request.method == "POST":
        file = request.files.get("image")

        if file and file.filename != "":
            # Unique filename (prevents overwrite)
            filename = str(int(time.time())) + "_" + file.filename
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(image_path)

            # Load image safely
            image = Image.open(image_path).convert("RGB")

            # Process with CLIP
            inputs = processor(
                text=labels,
                images=image,
                return_tensors="pt",
                padding=True
            ).to(device)

            outputs = model(**inputs)
            probs = outputs.logits_per_image.softmax(dim=1)

            pred_idx = probs.argmax().item()
            confidence = round(probs[0][pred_idx].item() * 100, 2)

            prediction = "Crop" if pred_idx == 0 else "Not Crop"

            # Debug (optional)
            print("Prediction:", prediction, "| Confidence:", confidence)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        image_path=image_path
    )

if __name__ == "__main__":
    app.run(debug=True)