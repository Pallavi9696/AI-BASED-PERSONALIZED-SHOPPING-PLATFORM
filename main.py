from flask import Flask, render_template, request
import cv2
import numpy as np
import os
from PIL import Image
import base64
from werkzeug.exceptions import RequestEntityTooLarge

app = Flask("personal_stylist_ai")

# ------------ FIX 1: Increase Upload + Form Size Limits ------------
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200MB
app.config['MAX_FORM_MEMORY_SIZE'] = 200 * 1024 * 1024

# Upload folder
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ------------ FIX 2: Handle Too Large Error ------------
@app.errorhandler(RequestEntityTooLarge)
def handle_large_file(e):
    return "Captured image is too large. Please try again.", 413


# Haarcascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


# -------------- SKIN TONE -----------------
def detect_skin_tone(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((100, 100))
    pixels = np.array(img).reshape((-1, 3))
    r, g, b = np.mean(pixels, axis=0)

    if r > g and r > b:
        return "Warm"
    elif b > r and b > g:
        return "Cool"
    else:
        return "Neutral"


# -------------- BODY TYPE -----------------
def detect_body_type(image_path):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    ratio = w / h

    if ratio < 0.45:
        return "Pear Body Type"
    elif ratio > 0.65:
        return "Apple Body Type"
    else:
        return "Hourglass Body Type"


# -------------- RECOMMENDATIONS -----------------
def get_recommendations(skin, body):
    recommendations = {}

    if skin == "Warm":
        recommendations['makeup'] = "Peach blush, nude lipstick, golden eyeshadow"
        recommendations['colors'] = "olive, mustard, warm brown"
    elif skin == "Cool":
        recommendations['makeup'] = "Pink blush, berry lipstick, silver eyeshadow"
        recommendations['colors'] = "blue, purple, cool grey"
    else:
        recommendations['makeup'] = "Neutral shades, brown eyeshadow"
        recommendations['colors'] = "beige, white, tan"

    if body == "Pear Body Type":
        recommendations['outfits'] = "A-line dresses, off-shoulder tops"
    elif body == "Apple Body Type":
        recommendations['outfits'] = "V-neck tops, empire waist dresses"
    else:
        recommendations['outfits'] = "Bodycon dresses, fitted outfits"

    return recommendations


# -------------------- HOME ROUTE --------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------- CAMERA CAPTURE --------------------
@app.route("/capture", methods=["POST"])
def capture_image():
    data = request.form['image']
    data = data.split(",")[1]  # remove base64 header
    img_bytes = base64.b64decode(data)

    filepath = os.path.join(UPLOAD_FOLDER, "camera.jpg")
    with open(filepath, "wb") as f:
        f.write(img_bytes)

    skin = detect_skin_tone(filepath)
    body = detect_body_type(filepath)
    rec = get_recommendations(skin, body)

    return render_template(
        "index.html",
        uploaded_image="camera.jpg",
        skin=skin,
        body=body,
        rec=rec
    )


# -------------------- FILE UPLOAD ROUTE --------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["photo"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    skin = detect_skin_tone(path)
    body = detect_body_type(path)
    rec = get_recommendations(skin, body)

    return render_template(
        "index.html",
        uploaded_image=file.filename,
        skin=skin,
        body=body,
        rec=rec
    )


if __name__ == "__main__":
    app.run(debug=True)
