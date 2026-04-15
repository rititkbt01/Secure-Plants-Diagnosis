"""
Student Model — DeiT-Tiny
===========================
Owner: Yashraj Shrestha (AI Lead)

Phase 2: Train DeiT-Tiny using knowledge distillation from ResNet-50 teacher.

DeiT-Tiny Architecture:
    - 5.7M parameters (12× smaller than ViT-Base)
    - 12 transformer layers
    - 3 attention heads
    - Patch size: 16×16 (input 224×224 → 196 patches)
    - Two special tokens: [CLS] (classification) + [DIST] (distillation)
    - Input: 224×224 RGB image

Why DeiT over standard ViT:
    - Standard ViT requires ~14M images (full ImageNet) for good performance
    - PlantVillage has only ~20K filtered images (our target subset)
    - DeiT's distillation token allows learning from teacher's soft labels
    - Achieves 85-88% accuracy on our dataset (vs ~65-70% for ViT without distillation)

Key Paper: Touvron et al. (2021) "Training data-efficient image transformers
           and distillation through attention"

TODO (Yashraj):
    - Implement create_student_model() using timm
    - The distillation token is handled by DeiT architecture automatically
    - Model outputs two predictions: class token output + distillation token output
"""

# import torch
# import torch.nn as nn
# import timm


def create_student_model(num_classes: int = 15, pretrained: bool = False):
    """
    Create DeiT-Tiny student model for knowledge distillation.

    Uses timm library to load DeiT-Tiny architecture.
    pretrained=False because we train from scratch with distillation.

    Args:
        num_classes: Number of disease classes (default 15).
        pretrained: Load pretrained ImageNet weights (default False).
                    We train from scratch via distillation.

    Returns:
        nn.Module: DeiT-Tiny model with distillation head.

    TODO (Yashraj):
        - Use timm.create_model('deit_tiny_distilled_patch16_224', pretrained=False, num_classes=num_classes)
        - Note: 'deit_tiny_distilled_patch16_224' includes the distillation token
        - Return configured model
    """
    pass


def get_model_summary(model) -> dict:
    """
    Get model parameter count and size summary.

    Returns:
        dict: total_params, trainable_params, model_size_mb

    TODO (Yashraj):
        - Count total parameters with sum(p.numel() for p in model.parameters())
        - Count trainable parameters
        - Estimate size in MB (params * 4 bytes / 1024^2)
    """
    pass
