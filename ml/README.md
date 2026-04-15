# ML Pipeline — DeiT-Tiny Knowledge Distillation

**Owners:**
- **Yashraj Shrestha** — AI Lead (DeiT-Tiny architecture, knowledge distillation)
- **Rishi Kumar Kushwaha** — Data Engineering Lead (dataset, augmentation pipeline)
- **Rishav Dhakal** — Model Optimization Lead (benchmarking, latency)

## Overview

Two-phase training strategy:

### Phase 1 — Teacher Model (ResNet-50)
Train a CNN teacher on PlantVillage dataset.
CNNs need less data due to inductive biases (translation equivariance, local receptive fields).
```bash
python scripts/train_teacher.py
# Output: models/teacher/resnet50_plant_teacher.pth
```

### Phase 2 — Student Distillation (DeiT-Tiny)
Train DeiT-Tiny using knowledge distillation from the ResNet-50 teacher.
Soft probability labels from teacher allow transformer to learn inter-class relationships.
```bash
python scripts/train_student.py
# Output: models/student/deit_tiny_plant_diagnosis.pth
```

## Full Training Guide
See: [docs/setup/model-training-setup.md](../docs/setup/model-training-setup.md)

## Performance Targets
| Metric | Target |
|--------|--------|
| Accuracy | ≥ 85% |
| F1-Score | ≥ 0.88 |
| Inference time | < 3 seconds |
