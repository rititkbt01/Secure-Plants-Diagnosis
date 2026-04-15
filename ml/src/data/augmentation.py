"""
Data Augmentation Pipeline
============================
Owner: Rishi Kumar Kushwaha (Data Engineering Lead)

Defines image transforms for training and validation/inference.

CRITICAL: Training transforms include augmentation (for generalization).
          Validation/inference transforms do NOT include augmentation.
          The inference transforms MUST match what is used in image_processing.py.

Augmentation Strategy (bridges lab-to-field domain gap):
    - Random Horizontal Flip (p=0.5) — leaf orientation variance
    - Random Crop 224x224 from 256x256 — scale invariance
    - Color Jitter — lighting variance (field vs. lab conditions)
    - Random Rotation ±15° — leaf angle variance
    - Gaussian Blur (p=0.3) — camera focus variance
    - ImageNet Normalization — matches pretrained feature distributions

References:
    - Singh et al. (2024): augmentation improves ViT generalization by 3-5%
    - Yang et al. (2024): mobile deployment augmentation strategy

TODO (Rishi):
    - Define get_train_transforms() with full augmentation
    - Define get_val_transforms() WITHOUT augmentation (just resize + normalize)
    - These must be consistent with image_processing.py in backend
"""

# from torchvision import transforms


# ImageNet normalization statistics (used for all transforms)
IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD  = [0.229, 0.224, 0.225]


def get_train_transforms():
    """
    Training transforms with data augmentation.

    Applied ONLY during model training to improve generalization.
    Simulates real-world field conditions (varied lighting, angles, focus).

    Returns:
        torchvision.transforms.Compose: Training transform pipeline.

    TODO (Rishi):
        - transforms.Compose([
            transforms.Resize(256),
            transforms.RandomCrop(224),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3),
            transforms.RandomRotation(degrees=15),
            transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 2.0)),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
          ])
    """
    pass


def get_val_transforms():
    """
    Validation/inference transforms WITHOUT augmentation.

    Used for: validation during training, test evaluation, and backend inference.
    MUST match the transforms in backend/app/services/image_processing.py.

    Returns:
        torchvision.transforms.Compose: Validation transform pipeline.

    TODO (Rishi):
        - transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
          ])
    """
    pass
