# Model Training Setup — Kaggle & Google Colab

This guide explains how to train the ResNet-50 teacher model and
DeiT-Tiny student model using free cloud GPU resources.

---

## Overview

| Phase | Model | Platform | Est. Time |
|-------|-------|----------|-----------|
| Phase 1 | ResNet-50 Teacher | Kaggle (T4 GPU) | 3–4 hours |
| Phase 2 | DeiT-Tiny Student | Kaggle (T4 GPU) | 4–5 hours |

---

## Dataset: PlantVillage

- **Images:** 54,306 color images
- **Classes:** 38 (we filter to 15 classes: 3 crops)
- **Source:** [Kaggle PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)
- **License:** Creative Commons BY 4.0

### Download to `data/raw/`
```bash
cd ml
python src/data/download.py --dataset plantvillage --output ../data/raw/
```

Or manually from Kaggle:
1. Go to https://www.kaggle.com/datasets/emmarex/plantdisease
2. Download and extract to `data/raw/PlantVillage/`

---

## Dataset: PlantDoc (Validation)

- **Images:** 2,598 field-condition images
- **Source:** [GitHub - PlantDoc](https://github.com/pratikkayal/PlantDoc-Dataset)
- **Purpose:** Evaluate real-world generalization

---

## Data Split Strategy

| Split | Percentage | Purpose |
|-------|-----------|---------|
| Train | 70% | Model training |
| Validation | 15% | Hyperparameter tuning |
| Test | 15% | Final evaluation (held-out) |

---

## Training on Kaggle

### Step 1: Upload dataset to Kaggle
1. Create account at https://www.kaggle.com
2. Upload PlantVillage dataset to your Kaggle datasets

### Step 2: Upload training notebooks
Upload from `ml/notebooks/`:
- `03_teacher_training.ipynb` (Phase 1)
- `04_student_distillation.ipynb` (Phase 2)

### Step 3: Enable GPU
- In Kaggle notebook: `Settings → Accelerator → GPU T4 x2`

### Step 4: Run Phase 1 — Teacher Training
```python
# In 03_teacher_training.ipynb
# Trains ResNet-50 on PlantVillage (filtered 15 classes)
# Expected accuracy: 85-90%
# Output: models/teacher/resnet50_plant_teacher.pth
```

### Step 5: Run Phase 2 — Student Distillation
```python
# In 04_student_distillation.ipynb
# Trains DeiT-Tiny using soft labels from ResNet-50 teacher
# Knowledge Distillation: alpha=0.7, temperature=4
# Expected accuracy: 85-88%
# Output: models/student/deit_tiny_plant_diagnosis.pth
```

---

## Training Configuration

See `ml/configs/` for YAML config files:

| Config | Description |
|--------|-------------|
| `teacher_config.yaml` | ResNet-50 hyperparameters |
| `student_config.yaml` | DeiT-Tiny + distillation params |
| `augmentation_config.yaml` | Data augmentation settings |

### Key Hyperparameters (DeiT Student)
| Parameter | Value | Reason |
|-----------|-------|--------|
| Learning rate | 0.0001 | Small LR for stable distillation |
| Batch size | 32 | Fits T4 GPU memory |
| Epochs | 50 | With early stopping (patience=10) |
| Distillation alpha | 0.7 | 70% soft labels, 30% hard labels |
| Temperature | 4 | Softens probability distributions |
| Input size | 224×224 | DeiT-Tiny standard input |
| Optimizer | AdamW | Standard for transformers |

---

## After Training: Export Model

```bash
cd ml
python scripts/export.py --model student --output ../models/student/
```

This exports the model for deployment with FastAPI.

---

## Saving Model Weights

⚠️ Model weight files (`.pth`) are **gitignored** (too large for Git).

Store them in:
- `models/teacher/resnet50_plant_teacher.pth`
- `models/student/deit_tiny_plant_diagnosis.pth`

Back up to:
- Kaggle dataset (versioned)
- Google Drive (team shared folder)
- Local machine

See `models/README.md` for download links once training is complete.
