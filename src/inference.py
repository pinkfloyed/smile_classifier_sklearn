from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import os
import pickle
import numpy as np
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

MODEL_DIR = "model"
IMG_SIZE = (64, 64)

try:
    with open(os.path.join(MODEL_DIR, "smile_classifier.pkl"), "rb") as model_file:
        model = pickle.load(model_file)
    with open(os.path.join(MODEL_DIR, "scaler.pkl"), "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    logging.info("Model and scaler loaded successfully.")
except FileNotFoundError as e:
    logging.error(f"Error loading model or scaler: {e}")
    exit(1)

def preprocess_image(image_path):
    if not os.path.exists(image_path):
        logging.error(f"Image file not found: {image_path}")
        exit(1)
    
    try:
        image = Image.open(image_path).convert("L")  # Convert to grayscale
        image = image.resize(IMG_SIZE)  # Resize to match model input size
        image_array = np.array(image).flatten().reshape(1, -1)  # Flatten the image
        logging.info("Image preprocessed successfully.")
        return scaler.transform(image_array)  # Apply the scaler
    except Exception as e:
        logging.error(f"Error processing image: {e}")
        exit(1)

def classify_image(image_path):
    features = preprocess_image(image_path)
    try:
        prediction = model.predict(features)
        logging.info("Image classified successfully.")
        return "Smiling" if prediction[0] == 1 else "Not Smiling"
    except Exception as e:
        logging.error(f"Error during classification: {e}")
        exit(1)

if __name__ == "__main__":
    image_path = r"D:\smile\data\non_smile\Aaron_Eckhart_0001.jpg"
    if not os.path.exists(image_path):
        logging.error(f"Image file does not exist: {image_path}")
        exit(1)

    result = classify_image(image_path)
    print(f"Prediction: {result}")
