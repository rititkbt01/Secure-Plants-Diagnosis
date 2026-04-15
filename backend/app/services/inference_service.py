"""
Inference Service — DeiT-Tiny Plant Disease Classification
==========================================================
Owner: Yashraj Shrestha (AI Lead)
       Integrated by: Ritik Budhathoki (Backend)

Loads the trained DeiT-Tiny model and runs inference on preprocessed
image tensors.

Model Details:
    - Architecture: DeiT-Tiny (Data-Efficient Image Transformer)
    - Parameters: ~5.7M
    - Input: 224×224 RGB image tensor
    - Output: Softmax probabilities over 15 disease classes
    - Training: Knowledge distillation from ResNet-50 teacher
    - Training Data: PlantVillage (filtered 15 classes)

Performance Target:
    - Accuracy: ≥ 85%
    - Inference time: < 3 seconds (end-to-end)

TODO (Yashraj + Ritik):
    - Implement load_model() to load .pth weights
    - Implement predict() to run forward pass and return (class, confidence)
    - Handle model not loaded gracefully
    - Add device selection (CPU/CUDA from config)
"""

import torch
# import timm
# from app.config import settings

# Disease class mapping (index → class name)
DISEASE_CLASSES = {
    0: "tomato_bacterial_spot",
    1: "tomato_early_blight",
    2: "tomato_late_blight",
    3: "tomato_leaf_mold",
    4: "tomato_septoria_leaf_spot",
    5: "tomato_spider_mites",
    6: "tomato_target_spot",
    7: "tomato_yellow_leaf_curl_virus",
    8: "tomato_mosaic_virus",
    9: "tomato_healthy",
    10: "potato_early_blight",
    11: "potato_late_blight",
    12: "potato_healthy",
    13: "pepper_bacterial_spot",
    14: "pepper_healthy",
}

# Global model variable (loaded once at startup)
_model = None


def load_model():
    """
    Load DeiT-Tiny model weights from disk into memory.

    Called once during FastAPI startup event.
    Model stays in memory for the lifetime of the server process.

    Raises:
        FileNotFoundError: If model weights file not found at MODEL_PATH.
        RuntimeError: If model cannot be loaded (corrupt file, version mismatch).

    TODO (Yashraj):
        - Use timm.create_model('deit_tiny_patch16_224', pretrained=False, num_classes=15)
        - Load state_dict from settings.MODEL_PATH
        - Set model to eval() mode
        - Move to settings.INFERENCE_DEVICE (cpu/cuda)
        - Set global _model variable
    """
    global _model
    # TODO (Yashraj): Implement model loading
    pass


def predict(image_tensor) -> tuple[str, float]:
    """
    Run DeiT-Tiny inference on a preprocessed image tensor.

    Args:
        image_tensor: PyTorch tensor of shape (1, 3, 224, 224),
                      normalized with ImageNet mean/std.

    Returns:
        tuple: (disease_class: str, confidence: float)
               e.g., ("tomato_early_blight", 0.923)

    Raises:
        RuntimeError: If model is not loaded.
        ValueError: If tensor shape is incorrect.

    TODO (Yashraj):
        - Check _model is not None
        - Move tensor to inference device
        - Run model forward pass (no_grad context)
        - Apply softmax to get probabilities
        - Get argmax for predicted class index
        - Return (DISEASE_CLASSES[class_idx], confidence_score)
    """
    global _model

    if _model is None:
        raise RuntimeError("Model not loaded. Call load_model() first.")

    # TODO (Yashraj): Implement inference
    pass
