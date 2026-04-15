"""
Knowledge Distillation Framework
==================================
Owner: Yashraj Shrestha (AI Lead)

Implements the knowledge distillation training paradigm from:
Hinton, Vinyals & Dean (2015) "Distilling the knowledge in a neural network"
Touvron et al. (2021) DeiT

How Knowledge Distillation Works:
    The student (DeiT-Tiny) learns from TWO supervisors simultaneously:
    
    1. Hard Labels (ground truth):
       Standard cross-entropy loss with one-hot class labels.
       Tells student "this leaf has Early Blight".
    
    2. Soft Labels (teacher knowledge):
       KL divergence loss between student and teacher probability distributions.
       Teacher soft output: [0.70 Early_Blight, 0.25 Late_Blight, 0.05 others]
       This encodes "Early Blight is visually similar to Late Blight".
       The student learns these fine-grained similarities — not just hard categories.

Combined Loss:
    total_loss = (1 - alpha) * hard_loss + alpha * soft_loss
    
    alpha = 0.7 (from our config) → 70% teacher knowledge, 30% ground truth
    temperature = 4 (softens teacher distributions for richer inter-class signal)

TODO (Yashraj):
    - Implement DistillationLoss class
    - Implement forward() combining hard and soft losses
    - Implement compute_soft_targets() with temperature scaling
"""

# import torch
# import torch.nn as nn
# import torch.nn.functional as F


class DistillationLoss:
    """
    Combined knowledge distillation loss for DeiT student training.

    Combines:
        - Hard label loss (CrossEntropy with ground truth)
        - Soft label loss (KL Divergence with teacher soft labels)

    Args:
        alpha: Weight for soft label loss (default 0.7).
               1.0 = all teacher, 0.0 = all hard labels.
        temperature: Softmax temperature for soft labels (default 4).

    TODO (Yashraj):
        - Implement __init__ to store alpha and temperature
        - Implement compute() to calculate combined loss
    """

    def __init__(self, alpha: float = 0.7, temperature: float = 4.0):
        # TODO (Yashraj): Store alpha and temperature
        pass

    def compute(self, student_logits, teacher_soft_labels, hard_labels):
        """
        Compute combined distillation loss.

        Args:
            student_logits: Raw output from DeiT-Tiny student model.
            teacher_soft_labels: Soft probabilities from ResNet-50 teacher.
            hard_labels: Ground truth class indices (one-hot equivalent).

        Returns:
            tuple: (total_loss, hard_loss, soft_loss) for logging.

        Formula:
            hard_loss = CrossEntropy(student_logits, hard_labels)
            soft_loss = KLDiv(softmax(student/T), softmax(teacher/T)) * T^2
            total_loss = (1 - alpha) * hard_loss + alpha * soft_loss

        TODO (Yashraj):
            - Compute hard_loss with nn.CrossEntropyLoss
            - Compute soft_loss with nn.KLDivLoss
                * Note: scale by T^2 to account for gradient scaling (Hinton et al.)
            - Return combined loss
        """
        pass
