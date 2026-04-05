# document-validation-study

A clean, generic study of the computer-vision techniques used to validate and
process portrait photographs.  All project-specific details have been removed so
this repository is safe for public storage.

---

## Project layout

```
document-validation-study/
├── notebooks/
│   ├── 01_flash_detection.ipynb      # Glare / flash-spot detection (OpenCV)
│   └── 02_photograph_pipeline.ipynb  # End-to-end 6-step portrait pipeline
├── scripts/
│   ├── rename.js                     # Sequential file renaming utility (Node.js)
│   └── structure.js                  # train / val / test dataset splitter (Node.js)
└── data/
    ├── input/                        # Place your images here
    └── output/                       # All results land here
        ├── glares/                   # Annotated glare-detection results
        └── pipeline/                 # Intermediate and final pipeline outputs
            ├── face_crop/
            ├── resize/
            └── remove_bg/
```

---

## Setup

### Python environment

```bash
# Create a virtual environment (uv is recommended)
uv venv .venv && source .venv/bin/activate   # macOS / Linux
# or: python -m venv .venv && .venv\Scripts\activate  # Windows

# Install dependencies
uv pip install "rembg[cpu]" mtcnn tensorflow opencv-python Pillow matplotlib
```

> **GPU acceleration** — switch to `rembg[gpu]` and pass
> `providers=["CUDAExecutionProvider"]` to `new_session()` in the notebook.

### Node.js environment (for scripts)

```bash
# Node 18+ is required; no extra packages needed.
node --version
```

---

## Notebooks

### 01_flash_detection.ipynb

Detects bright glare / flash regions in a photograph.

**Algorithm:**
1. Convert to grayscale.
2. Threshold bright pixels (> 225) → bright mask.
3. Detect low-texture regions via Laplacian variance → smooth mask.
4. Combine masks with bitwise-AND.
5. Morphological close + dilate to reconnect streaks.
6. Filter contours by area, edge density, and contrast.
7. Draw rounded red bounding boxes + labels.

**Config cell:**
```python
INPUT_IMAGE = "../data/input/sample_001.jpg"   # ← your image
OUTPUT_DIR  = "../data/output/glares"
```

---

### 02_photograph_pipeline.ipynb

Full end-to-end portrait validation and processing pipeline.

| Step | What it does |
|------|-------------|
| 1 | **Face count check** — MTCNN; raises error on 0 or >1 face |
| 2 | **Auto-correct orientation** — 0/90/180/270° scoring via MTCNN keypoints (disabled by default; enable by uncommenting) |
| 3 | **Face crop** — dynamic-margin bounding box around the largest detected face |
| 4 | **Blur detection** — Laplacian variance; stops pipeline below threshold |
| 5 | **Resize** — proportional scale with white background composite |
| 6 | **Background removal** — rembg `birefnet-portrait` with alpha-edge feathering |

**Config cell:**
```python
IMAGE_NAME = "sample_001.jpg"   # ← your image filename
INPUT_DIR  = "../data/input"
```

---

## Scripts

### scripts/structure.js

Splits raw images into an organised `train / val / test` dataset.

- Reads images from `../data/input/`
- Groups by document type (prefix before the first `_` in the filename)
- Copies files into `../data/output/<type>/{train,val,test}/`

**Convention:** name your raw files as `<type>_<anything>.<ext>`,
e.g. `id_001.jpg`, `permit_scan_002.png`.

```bash
cd scripts
node structure.js
```

---

### scripts/rename.js

Sequentially renames all images inside an organised dataset:
`001.jpg`, `002.jpg`, `003.jpg`, …

Run **after** `structure.js` to normalise filenames.

```bash
cd scripts
node rename.js
```

---

## Key concepts

| Concept | Library | Notes |
|---------|---------|-------|
| Face detection & keypoints | `mtcnn` | Returns bounding box + 5 landmarks |
| Glare / blur detection | `opencv-python` | Laplacian variance, thresholding |
| Background removal | `rembg` | `birefnet-portrait` model |
| Image matting | `Pillow` | Alpha compositing onto white background |
| Pipeline benchmarking | `time.perf_counter()` | Per-step and total wall-clock timing |
