import os
import numpy as np
import cv2
import base64
from flask import Flask, request, render_template, redirect
from tensorflow.keras.models import load_model
import tensorflow as tf

app = Flask(__name__)

# Load trained model
model = load_model("C:/Users/Vineela/Desktop/homotovision/chatbot/Bloodcell2.h5")

# Class labels (make sure this order matches your training data)
class_labels = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']

# Ensure 'static' folder exists
os.makedirs("static", exist_ok=True)

# Feature extractor using HSV histograms
def extract_features(img):
    img = cv2.resize(img, (64, 64))
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    hist_h = cv2.calcHist([hsv], [0], None, [7], [0, 180])
    hist_s = cv2.calcHist([hsv], [1], None, [7], [0, 256])
    hist_v = cv2.calcHist([hsv], [2], None, [6], [0, 256])
    features = np.concatenate([hist_h, hist_s, hist_v]).flatten()
    features = features / np.sum(features)  # Normalize
    return features.reshape(1, -1)

# Predict class from image path
def predict_image_class(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image could not be read.")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        features = extract_features(img_rgb)

        predictions = model.predict(features)
        probs = tf.nn.softmax(predictions).numpy()[0]

        idx = np.argmax(probs)
        predicted_label = class_labels[idx]

        return predicted_label, img_rgb

    except Exception as e:
        return str(e), None

# Flask route for uploading image
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files.get("file")
        if not f or f.filename == "":
            return redirect(request.url)

        path = os.path.join("static", f.filename)
        f.save(path)

        predicted, img_rgb = predict_image_class(path)

        if img_rgb is None:
            return f"Error: {predicted}", 400

        _, enc = cv2.imencode('.png', cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))
        img_str = base64.b64encode(enc).decode('utf-8')

        return render_template("result.html", class_label=predicted, img_data=img_str)

    return render_template("home.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
