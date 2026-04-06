
# 🌿 Crop vs Non-Crop Detection using Deep Learning and VLM

This project is a web-based application that classifies whether an input image contains **agricultural crops or not**.

It uses:
- ✅ A **trained CNN model (ResNet18)** for accurate classification  
- ✅ A **Vision-Language Model (CLIP)** for flexible, zero-shot prediction (optional)

---

# 🚀 Features

- Upload an image through a web interface
- Predict whether the image is:
  - 🌱 Crop
  - ❌ Not Crop
- Clean and responsive UI
- Supports:
  - Trained model (high accuracy)
  - VLM (CLIP) for zero-shot classification

---

# 🧠 Technologies Used

- Python
- PyTorch
- Torchvision
- Flask (Web Framework)
- Hugging Face Transformers (for VLM)
- HTML, CSS (Frontend)

---

# 🏗️ Project Structure
# 🌿 Crop vs Non-Crop Detection using Deep Learning and VLM

This project is a web-based application that classifies whether an input image contains **agricultural crops or not**.

It uses:
- ✅ A **trained CNN model (ResNet18)** for accurate classification  
- ✅ A **Vision-Language Model (CLIP)** for flexible, zero-shot prediction (optional)

---

# 🚀 Features

- Upload an image through a web interface
- Predict whether the image is:
  - 🌱 Crop
  - ❌ Not Crop
- Clean and responsive UI
- Supports:
  - Trained model (high accuracy)
  - VLM (CLIP) for zero-shot classification

---

# 🧠 Technologies Used

- Python
- PyTorch
- Torchvision
- Flask (Web Framework)
- Hugging Face Transformers (for VLM)
- HTML, CSS (Frontend)

---

# 🏗️ Project Structure
# 🌿 Crop vs Non-Crop Detection using Deep Learning and VLM

This project is a web-based application that classifies whether an input image contains **agricultural crops or not**.

It uses:
- ✅ A **trained CNN model (ResNet18)** for accurate classification  
- ✅ A **Vision-Language Model (CLIP)** for flexible, zero-shot prediction (optional)

---

# 🚀 Features

- Upload an image through a web interface
- Predict whether the image is:
  - 🌱 Crop
  - ❌ Not Crop
- Clean and responsive UI
- Supports:
  - Trained model (high accuracy)
  - VLM (CLIP) for zero-shot classification

---

# 🧠 Technologies Used

- Python
- PyTorch
- Torchvision
- Flask (Web Framework)
- Hugging Face Transformers (for VLM)
- HTML, CSS (Frontend)

---

# 🏗️ Project Structure
new_work/
├── app.py # Flask web app
├── train.py # Model training script
├── predict.py # Local prediction script
├── crop_model.pth # Trained model
├── static/ # Uploaded images
└── templates/
└── index.html # UI page

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/crop-detection.git
cd crop-detection
2. Install dependencies
pip install torch torchvision flask pillow transformers==4.36.2
🏋️ Model Training

Run:

python train.py

This will:

Train a ResNet18 model
Save it as crop_model.pth
🔍 Local Prediction

Test using:

python predict.py

Example output:

crop
🌐 Run Web Application
python app.py

Open browser:

http://127.0.0.1:5000
🧪 How It Works
🔹 1. CNN Model (ResNet18)
Trained on labeled dataset
Learns features specific to crops
Provides high accuracy
Pipeline:
Image → Resize → Tensor → ResNet18 → Prediction
🔹 2. Vision-Language Model (CLIP)
Uses Hugging Face openai/clip-vit-base-patch32
No training required
Compares image with text prompts
Example:
Text:
- "agricultural crops"
- "non agricultural scene"

→ Model selects most similar
📊 Comparison
Model	Accuracy	Flexibility	Training
ResNet18	✅ High	❌ Fixed	Required
CLIP (VLM)	⚠️ Medium	✅ Flexible	Not required
⚠️ Limitations
ResNet Model
Requires sufficient dataset
May fail on unseen conditions
VLM (CLIP)
Can confuse:
Forest vs crops
Close-up leaves
Depends heavily on text prompts
📈 Future Improvements
Combine ResNet + CLIP (Hybrid system)
Add confidence visualization
Deploy online (Render / AWS)
Improve dataset diversity
Use advanced models (EfficientNet / ViT)
🧠 Key Learnings
Difference between CNN vs VLM
Importance of dataset quality
Real-world issues like:
preprocessing mismatch
model generalization
📸 Example Outputs
Input Image	Prediction
Farm Field	Crop ✅
Road/City	Not Crop ❌
📌 Conclusion

This project demonstrates:

Practical deep learning deployment
Comparison between supervised models and VLMs
Real-world web integration using Flask
👨‍💻 Author:Manish


⭐ If you like this project

Give it a star ⭐ on GitHub!

---

- Covers **both models (CNN + VLM)** → shows depth  
- Includes **comparison table** → looks professional  
- Explains **how it works technically** → good for evaluation  
- Clean structure → easy for recruiters/professors  

---

# If you want next level

I can upgrade this with:
- screenshots section  
- demo GIF  
- deployment instructions (Render / Hugging Face Spaces)  
- research-style explanation  

Just tell me 👍
