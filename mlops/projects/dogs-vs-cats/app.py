from contextlib import asynccontextmanager
from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import cv2
import os
import uvicorn

MODEL_PATH = os.getenv("MODEL_PATH", "cat_vs_dog_model.h5")
model = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the model on startup and release on shutdown."""
    global model
    print(f"Loading model from: {MODEL_PATH} ...")
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully!")
    yield
    model = None


app = FastAPI(
    title="Cat vs Dog Classifier",
    description="Upload an image and get a cat/dog prediction.",
    version="1.0.0",
    lifespan=lifespan,
)


# ── Response schema ────────────────────────────────────────────────────────────
class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    raw_score: float
    message: str


# ── Helpers ────────────────────────────────────────────────────────────────────
def preprocess_image(img_bytes: bytes) -> np.ndarray:
    """Decode and preprocess the uploaded image for prediction."""
    img_array = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Could not decode image. Ensure it is a valid image file.")
    img = cv2.resize(img, (256, 256))
    img = img.reshape((1, 256, 256, 3))
    img = img.astype("float32") / 255.0
    return img


# ── Endpoints ──────────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    """Health-check endpoint."""
    return {"status": "healthy", "model": MODEL_PATH}


@app.post("/predict", response_model=PredictionResponse)
async def predict(image: UploadFile = File(..., description="Cat or dog image")):
    """
    Predict whether the uploaded image is a cat or a dog.

    - **image**: image file (JPEG, PNG, …)
    """
    img_bytes = await image.read()

    try:
        img = preprocess_image(img_bytes)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    try:
        prediction = model.predict(img)
        score = float(prediction[0][0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

    # score → 0 = cat, score → 1 = dog
    if score > 0.5:
        label, confidence = "dog", score
    else:
        label, confidence = "cat", 1.0 - score

    return PredictionResponse(
        prediction=label,
        confidence=round(confidence, 4),
        raw_score=round(score, 4),
        message=f"This is a {label} with {round(confidence * 100, 2)}% confidence.",
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
