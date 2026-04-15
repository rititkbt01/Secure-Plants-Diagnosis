"""
Image Preprocessing Pipeline
==============================
Owner: Rishi Kumar Kushwaha (Data Engineering Lead)
       Integrated by: Ritik Budhathoki (Backend)

Transforms raw uploaded image bytes into a normalized PyTorch tensor
ready for DeiT-Tiny inference.

Preprocessing Steps (matching training transforms):
    1. Decode bytes → PIL Image
    2. Convert to RGB (handle RGBA/grayscale edge cases)
    3. Resize to 256×256
    4. Center crop to 224×224 (DeiT-Tiny input size)
    5. Convert to tensor (float32, range [0,1])
    6. Normalize: mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
       (ImageNet statistics — same as training)

Important: These transforms MUST match the validation transforms
           used during model training (not the augmented training transforms).

TODO (Rishi + Ritik):
    - Implement preprocess() function
    - Handle corrupt/invalid images gracefully
    - Verify output tensor shape is (1, 3, 224, 224)
"""

from io import BytesIO
# from PIL import Image
# import torch
# from torchvision import transforms


# Inference transforms (NO augmentation — matches val/test transforms from training)
# TODO (Rishi): Define inference_transforms matching training val transforms
inference_transforms = None  # TODO: Replace with actual transforms.Compose(...)


def preprocess(image_bytes: bytes):
    """
    Preprocess raw image bytes into a DeiT-ready tensor.

    Args:
        image_bytes: Raw bytes of the uploaded image file.

    Returns:
        torch.Tensor: Normalized tensor of shape (1, 3, 224, 224).

    Raises:
        ValueError: If image cannot be decoded or processed.

    TODO (Rishi):
        - Open image_bytes with PIL.Image.open(BytesIO(image_bytes))
        - Convert to RGB
        - Apply inference_transforms
        - Add batch dimension (unsqueeze(0))
        - Return tensor
    """
    pass


def get_image_info(image_bytes: bytes) -> dict:
    """
    Get basic metadata about an uploaded image.

    Args:
        image_bytes: Raw bytes of the uploaded image.

    Returns:
        dict: width, height, mode, format of the image.

    TODO (Rishi): Use PIL to extract image metadata
    """
    pass
