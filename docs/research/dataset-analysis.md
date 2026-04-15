# Dataset Analysis

## Datasets Used

### 1. PlantVillage (Primary Training)

| Property | Detail |
|----------|--------|
| Total images | 54,306 |
| Disease classes | 38 (across 14 crops) |
| Image type | Controlled laboratory (uniform background) |
| Image size | Variable (resized to 224×224 for training) |
| Format | JPEG/PNG |
| License | Creative Commons BY 4.0 |
| Source | https://www.kaggle.com/datasets/emmarex/plantdisease |

**Our filtered subset (15 classes — 3 crops):**

| Crop | Class | Approx. Count |
|------|-------|--------------|
| Tomato | Bacterial Spot | ~2,127 |
| Tomato | Early Blight | ~1,000 |
| Tomato | Late Blight | ~1,909 |
| Tomato | Leaf Mold | ~952 |
| Tomato | Septoria Leaf Spot | ~1,771 |
| Tomato | Spider Mites | ~1,676 |
| Tomato | Target Spot | ~1,404 |
| Tomato | Yellow Leaf Curl Virus | ~5,357 |
| Tomato | Mosaic Virus | ~373 |
| Tomato | Healthy | ~1,591 |
| Potato | Early Blight | ~1,000 |
| Potato | Late Blight | ~1,000 |
| Potato | Healthy | ~152 |
| Bell Pepper | Bacterial Spot | ~997 |
| Bell Pepper | Healthy | ~1,478 |

**Known Limitation:** Images are controlled/lab conditions.
Performance drops 15-20% on real field images (Singh et al., 2020).
We mitigate this with aggressive augmentation.

---

### 2. PlantDoc (Field Validation)

| Property | Detail |
|----------|--------|
| Total images | 2,598 |
| Image type | Real-world field conditions |
| Conditions | Varied lighting, backgrounds, leaf orientations |
| Purpose | Evaluating real-world generalization |
| Source | https://github.com/pratikkayal/PlantDoc-Dataset |

---

## Data Split

```
PlantVillage (filtered 15 classes)
├── train/    (70%) — used for training
├── val/      (15%) — used during training for hyperparameter tuning
└── test/     (15%) — held-out, NEVER seen during training
```

PlantDoc is used separately for cross-dataset generalization evaluation.

---

## Data Augmentation Strategy

Applied during training to bridge lab-to-field domain gap:

| Augmentation | Parameters | Purpose |
|-------------|-----------|---------|
| Random Horizontal Flip | p=0.5 | Leaf orientation variance |
| Random Crop | 224×224 from 256×256 | Scale invariance |
| Color Jitter | brightness±0.3, contrast±0.3, saturation±0.3 | Lighting variance |
| Random Rotation | ±15° | Leaf angle variance |
| Gaussian Blur | kernel=(3,3), sigma=(0.1,2.0), p=0.3 | Camera focus variance |
| Random Grayscale | p=0.1 | Disease pattern independence from color |
| Normalize | mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225] | ImageNet normalization |

See `ml/configs/augmentation_config.yaml` for full configuration.
See `ml/src/data/augmentation.py` for implementation.
