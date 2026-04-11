# ── Base image ────────────────────────────────────────────────────────────────
FROM python:3.10-slim

# ── Working directory ──────────────────────────────────────────────────────────
WORKDIR /app

# ── System dependencies needed by OpenCV headless ─────────────────────────────
RUN apt-get update && apt-get install -y --no-install-recommends \
        libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ── Python dependencies ────────────────────────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Application code ───────────────────────────────────────────────────────────
COPY app.py .

# ── Trained model (must exist in this directory before docker build) ───────────
# Run the notebook (cat-vs-dog.ipynb) to generate cat_vs_dog_model.h5 first.
COPY cat_vs_dog_model.h5 .

# ── Runtime configuration ──────────────────────────────────────────────────────
ENV MODEL_PATH=cat_vs_dog_model.h5
ENV PORT=5000

EXPOSE 5000

# ── Start the inference server (uvicorn) ──────────────────────────────────────
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
