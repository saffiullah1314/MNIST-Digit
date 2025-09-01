# 🧠 MNIST Digit Predictor ✍️  

A modern **Deep Learning web app** that recognizes handwritten digits (0–9) in real time using a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**.  
The interface is built with **Streamlit** and styled with a sleek **dark theme**, making digit prediction fast, accurate, and visually engaging.  

---

## 🚀 Live Demo  
🔗 [Try it here](https://mnist-digit-saffi.streamlit.app/)  

---

## 📌 Features  
- 🎨 **Interactive Drawing Board** – Draw digits directly on the canvas.  
- ⚡ **Real-Time Predictions** – Instantly predicts the digit with confidence score.  
- 🌑 **Dark Themed UI** – Modern gradient styling with animations for a smooth experience.  
- 📊 **High Accuracy CNN Model** – Achieves ~99% accuracy on MNIST test data.  
- 🖥 **Built with Streamlit** – Lightweight and deployable anywhere.  

---

## 🛠️ Tech Stack  
- **Python 3.9+**  
- **TensorFlow / Keras** – Model training & prediction  
- **OpenCV** – Image preprocessing  
- **NumPy** – Numerical operations  
- **Streamlit** – Web app frontend  
- **streamlit-drawable-canvas** – Drawing functionality  

---

## 📂 Project Structure  
```bash
MNIST-Digit-Predictor/
│── model/                   # Saved trained CNN model
│── main.py                  # Streamlit app (frontend + prediction)
│── requirements.txt         # Python dependencies
│── README.md                # Documentation
```
---

## ⚙️ Installation & Setup


**Clone the repo**
```bash
git clone https://github.com/your-username/MNIST-Digit.git
cd MNIST-Digit
```

**Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Run the app**
```bash
streamlit run main.py
```
---

## 📊 Model Overview

**Architecture:**

-  Convolutional layers

- MaxPooling layers

- Dense hidden layer with ReLU

- Output layer with Softmax (10 classes)

- Accuracy: ~99.7%
  
---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss your ideas.

---

## 📜 License

This project is licensed under the MIT License – free to use and modify.

⚡ Created with ❤️ by **Safi Ullah**
