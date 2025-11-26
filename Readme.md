# AI-BASED PERSONALIZED SHOPPING PLATFORM  
An AI-powered system for personalized fashion & makeup recommendations with **camera capture support**.

---

## 📌 Project Overview  
This project is a **Flask-based AI application** that provides fashion and makeup recommendations using image analysis.  
The system detects:

✔ Skin Tone  
✔ Body Type  
✔ Outfit Recommendations  
✔ Makeup Suggestions  
✔ Color Palette  
✔ Camera Capture + Image Upload Support  

It is built for **B.Tech Final Year Project** and runs fully in **VS Code**.

---

## 🚀 Features  

### 🎨 AI Features  
- Skin tone detection using RGB analysis  
- Body type classification (Pear, Apple, Hourglass)  
- Personalized outfit suggestions  
- Makeup + accessory recommendations  
- Recommendation engine based on detected attributes  

### 📸 Camera Features  
- Live camera preview (getUserMedia)  
- Capture & upload image instantly  
- Automatic compression to avoid *Request Entity Too Large* error  
- Saves captured photo in `/uploads` folder  

### 🖼 Upload Features  
- Upload from phone/laptop  
- Supports JPG, JPEG, PNG  

---

## 🗂 Project Structure  

AI-Fashion-Platform/
│── main.py
│── /templates
│ └── index.html
│── /static
│ └── styles.css
│── /uploads
│── /model (optional)
│── README.md


---

## 🛠 Technologies Used  

### 🔹 Backend  
- Python 3  
- Flask  

### 🔹 AI / Image Processing  
- OpenCV  
- Pillow (PIL)  
- NumPy  

### 🔹 Frontend  
- HTML  
- CSS  
- JavaScript (Camera API)  

---


### **3️⃣ Open in Browser**
http://127.0.0.1:5000/


---

## 📸 Camera Usage  
- Click **Capture** button  
- Camera photo compress hoke backend me jayega  
- AI model skin tone + body type detect karega  
- Output same page par dikh jayega  

---

## 🔍 AI Logic Explanation  

### **1. Skin Tone Detection**  
Image ko 100×100 resize → RGB average calculate →  
Rules:  
- R highest → Warm  
- B highest → Cool  
- Otherwise → Neutral  

### **2. Body Type Detection**  
Body image ka width/height ratio:  
- < 0.45 → Pear  
- > 0.65 → Apple  
- Else → Hourglass  




