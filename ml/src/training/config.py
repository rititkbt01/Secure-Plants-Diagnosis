"""
Training Hyperparameters
=========================
Owner: Yashraj Shrestha

Default hyperparameter values. Override via YAML config files in ml/configs/.
"""

# ── Phase 1: Teacher (ResNet-50) ─────────────────────────────────────────────
TEACHER_CONFIG = {
    "model": "resnet50",
    "num_classes": 15,
    "pretrained": True,              # ImageNet pretrained
    "learning_rate": 0.001,
    "batch_size": 32,
    "num_epochs": 30,
    "patience": 7,                   # Early stopping
    "label_smoothing": 0.1,
    "optimizer": "adamw",
    "weight_decay": 0.01,
    "save_path": "models/teacher/resnet50_plant_teacher.pth",
}

# ── Phase 2: Student (DeiT-Tiny) ──────────────────────────────────────────────
STUDENT_CONFIG = {
    "model": "deit_tiny_distilled_patch16_224",
    "num_classes": 15,
    "pretrained": False,             # Train from scratch via distillation
    "learning_rate": 0.0001,         # Lower LR for stable distillation
    "batch_size": 32,                # Fits T4 GPU memory
    "num_epochs": 50,
    "patience": 10,                  # Early stopping
    "distillation_alpha": 0.7,       # 70% soft labels, 30% hard labels
    "temperature": 4.0,              # Softmax temperature (Hinton et al., 2015)
    "optimizer": "adamw",
    "weight_decay": 0.05,
    "save_path": "models/student/deit_tiny_plant_diagnosis.pth",
}

# ── Data ──────────────────────────────────────────────────────────────────────
DATA_CONFIG = {
    "data_dir": "data/raw/PlantVillage",
    "train_ratio": 0.70,
    "val_ratio": 0.15,
    "test_ratio": 0.15,
    "random_seed": 42,               # For reproducibility
    "num_workers": 2,
    "input_size": 224,
}
