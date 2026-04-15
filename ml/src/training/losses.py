"""
Loss Functions
===============
Owner: Yashraj Shrestha

Defines loss functions for both training phases.

Phase 1 (Teacher): Standard Cross-Entropy Loss
Phase 2 (Student): Knowledge Distillation Loss (from distillation.py)

TODO (Yashraj):
    - Implement get_teacher_loss() — standard CrossEntropy
    - Implement get_student_loss() — returns DistillationLoss instance
    - Add label smoothing option for teacher training
"""

# import torch.nn as nn
# from ml.src.models.distillation import DistillationLoss


def get_teacher_loss(label_smoothing: float = 0.1):
    """
    Get loss function for Phase 1 (Teacher ResNet-50 training).

    Args:
        label_smoothing: Label smoothing factor (default 0.1 reduces overconfidence).

    Returns:
        nn.CrossEntropyLoss: Loss function for teacher training.

    TODO (Yashraj): Return nn.CrossEntropyLoss(label_smoothing=label_smoothing)
    """
    pass


def get_student_loss(alpha: float = 0.7, temperature: float = 4.0):
    """
    Get loss function for Phase 2 (Student DeiT distillation).

    Args:
        alpha: Weight for distillation loss (default 0.7).
        temperature: Knowledge distillation temperature (default 4.0).

    Returns:
        DistillationLoss: Combined hard + soft label loss function.

    TODO (Yashraj): Return DistillationLoss(alpha=alpha, temperature=temperature)
    """
    pass
