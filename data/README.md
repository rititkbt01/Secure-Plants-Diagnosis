# Data Directory

> ⚠️ **All dataset folders are gitignored — do NOT commit raw images to Git.**

## Structure
```
data/
├── raw/        ← Downloaded datasets (gitignored)
├── processed/  ← Cleaned and preprocessed data (gitignored)
└── splits/     ← Train/val/test split indices (gitignored)
```

## Downloading Datasets

### PlantVillage (Primary Training Data)
- **Source:** https://www.kaggle.com/datasets/emmarex/plantdisease
- **Size:** ~1.3GB
- **Images:** 54,306 across 38 classes
- **Our subset:** 15 classes (Tomato: 10, Potato: 3, Bell Pepper: 2)

**Steps:**
1. Download from Kaggle
2. Extract to `data/raw/PlantVillage/`
3. Verify structure: `python ml/src/data/download.py`

### PlantDoc (Field Validation)
- **Source:** https://github.com/pratikkayal/PlantDoc-Dataset
- **Size:** ~42MB
- **Images:** 2,598 real-world field images
- **Purpose:** Evaluating real-world generalization (not used in training)

**Steps:**
1. Clone or download PlantDoc repository
2. Extract to `data/raw/PlantDoc/`

## Licenses
- PlantVillage: Creative Commons Attribution 4.0 (CC BY 4.0)
- PlantDoc: For research/educational use only

## Data Pipeline
After downloading, run preprocessing:
```bash
cd ml
python src/data/download.py        # Verify dataset structure
jupyter notebook notebooks/02_data_preprocessing.ipynb
```
