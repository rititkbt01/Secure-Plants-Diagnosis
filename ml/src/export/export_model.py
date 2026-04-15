"""
Model Export for Deployment
=============================
Owner: Yashraj Shrestha + Rishav Dhakal

Exports trained DeiT-Tiny model for FastAPI backend deployment.

Export Format: PyTorch .pth state_dict
Destination: models/student/deit_tiny_plant_diagnosis.pth

The exported file is loaded by:
    backend/app/services/inference_service.py

TODO (Yashraj):
    - Implement export_student_model() to save state_dict
    - Implement validate_exported_model() to verify exported model runs correctly
    - Document model version and training configuration in metadata file
"""

import json
from pathlib import Path
# import torch


def export_student_model(model, save_path: str, metadata: dict = None):
    """
    Export trained DeiT-Tiny student model weights.

    Args:
        model: Trained DeiT-Tiny PyTorch model.
        save_path: Path to save .pth file.
        metadata: Optional training metadata to save alongside weights.

    TODO (Yashraj):
        - Save model.state_dict() to save_path
        - Save metadata (accuracy, training date, config) as JSON
    """
    pass


def validate_exported_model(model_path: str, num_classes: int = 15) -> bool:
    """
    Validate that exported model loads and runs correctly.

    Args:
        model_path: Path to exported .pth file.
        num_classes: Expected number of output classes.

    Returns:
        bool: True if model loads and forward pass succeeds.

    TODO (Yashraj):
        - Load model from path
        - Create random test tensor (1, 3, 224, 224)
        - Run forward pass
        - Verify output shape is (1, 15)
    """
    pass
