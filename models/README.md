# Models Directory

> ⚠️ **Model weight files (.pth) are gitignored — too large for Git (~87MB for DeiT-Tiny).**

## Structure
```
models/
├── teacher/    ← ResNet-50 teacher weights (gitignored)
│   └── resnet50_plant_teacher.pth
└── student/    ← DeiT-Tiny student weights (gitignored)
    └── deit_tiny_plant_diagnosis.pth
```

## How to Get Models

### Option 1: Train from Scratch
Follow the training guide: [docs/setup/model-training-setup.md](../docs/setup/model-training-setup.md)

```bash
# Phase 1: Train teacher (3-4 hours, Kaggle T4 GPU)
python ml/scripts/train_teacher.py

# Phase 2: Distill student (4-5 hours, Kaggle T4 GPU)
python ml/scripts/train_student.py
```

### Option 2: Download Pre-trained Weights (after training)
```
# TODO: Add Google Drive download link here after training
# wget -O models/student/deit_tiny_plant_diagnosis.pth <LINK>
```

## Model Details

| Model | File | Parameters | Purpose |
|-------|------|-----------|---------|
| ResNet-50 Teacher | `teacher/resnet50_plant_teacher.pth` | ~25M | Phase 1 teacher; generates soft labels |
| DeiT-Tiny Student | `student/deit_tiny_plant_diagnosis.pth` | ~5.7M | **Production model** for FastAPI backend |

## Backing Up Models

After training, back up to multiple locations:
1. Kaggle dataset (versioned)
2. Team Google Drive folder
3. Local machine

Do **NOT** commit model files to Git.
