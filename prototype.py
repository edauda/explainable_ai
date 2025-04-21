# XAI-Health Prototype (Streamlit Interface)
import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="XAI-Health Prototype", layout="centered")
st.title("🩺 XAI-Health: Breast Cancer Detection with Explainability")

# Sidebar instructions
st.sidebar.title("Navigation")
st.sidebar.info("Upload a breast scan image to get predictions and explanations. Provide your feedback below.")

# Upload Image
uploaded_file = st.file_uploader("Upload a breast scan image (JPEG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    image_array = np.array(image)

    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.subheader("Step 1: Prediction")
    st.write("🔍 Running model prediction...")

    # Fake prediction result (placeholder)
    prediction = "Malignant"
    confidence = 92.3
    st.success(f"**Prediction:** {prediction} (Confidence: {confidence}%)")

    st.subheader("Step 2: Visual Explanation")
    st.write("🧠 Generating Grad-CAM explanation...")

    try:
        # Generate grayscale version
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        gray_colored = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
        heatmap = cv2.addWeighted(image_array, 0.6, gray_colored, 0.4, 0)
        st.image(heatmap, caption="Grad-CAM Explanation (Simulated)", use_column_width=True)
    except Exception as e:
        st.error(f"Error generating heatmap: {e}")

    st.subheader("Step 3: Clinician Feedback")
    clarity = st.slider("How clear was the explanation?", 1, 5, 3)
    usefulness = st.slider("How helpful was the explanation for your diagnosis?", 1, 5, 3)
    confidence_boost = st.slider("Did this explanation increase your confidence in the prediction?", 1, 5, 3)
    comments = st.text_area("Any additional comments?")

    if st.button("Submit Feedback"):
        st.success("✅ Feedback submitted. Thank you!")
        # This would typically save to a database or feedback log
else:
    st.info("Please upload a medical image to begin.")
