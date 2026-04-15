"""
Phase 2: Train DeiT-Tiny Student via Knowledge Distillation
==============================================================
Owner: Yashraj Shrestha (AI Lead)

Trains DeiT-Tiny using soft labels from ResNet-50 teacher.

PREREQUISITE: ResNet-50 teacher must be trained first.
    Run: python ml/scripts/train_teacher.py

Usage:
    python ml/scripts/train_student.py
    python ml/scripts/train_student.py --config ml/configs/student_config.yaml

Output:
    models/student/deit_tiny_plant_diagnosis.pth

TODO (Yashraj):
    - Load trained teacher model
    - Generate soft labels from teacher
    - Train DeiT-Tiny student with DistillationLoss
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

# from ml.src.models.teacher import create_teacher_model, get_teacher_soft_labels
# from ml.src.models.student import create_student_model
# from ml.src.models.distillation import DistillationLoss
# from ml.src.training.trainer import Trainer


def main():
    """
    Main training script for DeiT-Tiny knowledge distillation.

    TODO (Yashraj):
        1. Load trained teacher from models/teacher/resnet50_plant_teacher.pth
        2. Create datasets and DataLoaders
        3. Generate teacher soft labels for training set
        4. Create DeiT-Tiny student model
        5. Create DistillationLoss (alpha=0.7, temperature=4.0)
        6. Train with combined hard + soft label loss
        7. Save student model to models/student/
    """
    print("Phase 2: DeiT-Tiny Knowledge Distillation")
    print("=" * 50)
    print("Prerequisite: ResNet-50 teacher must be trained first")
    print("TODO (Yashraj): Implement distillation training pipeline")


if __name__ == "__main__":
    main()
