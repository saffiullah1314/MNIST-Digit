import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import cv2
import tensorflow as tf
import time

st.set_page_config(page_title="Digit Predictor", page_icon="✍️", layout="centered")

model = tf.keras.models.load_model("MNIST_Digit_Trained_Model.keras", compile=False, safe_mode=False)

# 🔹 Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(135deg, #1DB954, #1ED760);
        color: white;
        border-radius: 10px;
        font-size: 18px;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background: linear-gradient(135deg, #1ED760, #1DB954);
    }
    .prediction-box {
        background: linear-gradient(135deg, #232526, #414345);
        padding: 25px;
        border-radius: 15px;
        text-align: left;
        margin-top: 20px;
        margin-right: 40px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.6);
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align:center;'>✍️ Draw a Digit</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>White box me digit draw karo aur Predict dabao</p>", unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="#FFFFFF",
    stroke_width=12,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("🔮 Predict"):
    if canvas_result.image_data is not None:
        img = cv2.cvtColor(canvas_result.image_data.astype("uint8"), cv2.COLOR_RGBA2GRAY)
        img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
        img = cv2.bitwise_not(img)
        img = img.astype("float32") / 255.0
        img = img.reshape(1, 28, 28, 1)

        with st.spinner("Predicting..."):
            time.sleep(1)
            prediction = model.predict(img)
            result = np.argmax(prediction)
            confidence = float(np.max(prediction) * 100)

        st.markdown(
            f"""
            <div class="prediction-box">
                <h2 style="color:#1ED760;">Predicted Digit: {result}</h2>
                <h4 style="color:#FFD700;">Confidence: {confidence:.2f}%</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )
