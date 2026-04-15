"""
Dataset Download Helper
========================
Owner: Rishi Kumar Kushwaha

Provides instructions and utilities for downloading PlantVillage and PlantDoc.

Note: Due to dataset size (~1GB), we do not auto-download.
      This script validates that the dataset is correctly placed.

TODO (Rishi):
    - Implement verify_plantvillage() to check folder structure
    - Print clear instructions for manual download
"""

import os
from pathlib import Path


EXPECTED_FOLDERS = [
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Potato___Early_Blight",
    "Potato___Late_blight",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    # ... (all 15 folders)
]


def verify_plantvillage(data_dir: str = "data/raw/PlantVillage") -> bool:
    """
    Verify PlantVillage dataset is correctly placed.

    Args:
        data_dir: Expected path to PlantVillage folder.

    Returns:
        bool: True if dataset is found and has expected structure.

    TODO (Rishi):
        - Check data_dir exists
        - Check at least 14 of the EXPECTED_FOLDERS exist
        - Print summary of found/missing folders
    """
    print("=" * 60)
    print("PlantVillage Dataset Setup")
    print("=" * 60)
    print("Download from: https://www.kaggle.com/datasets/emmarex/plantdisease")
    print(f"Extract to: {data_dir}/")
    print("=" * 60)

    # TODO (Rishi): Verify folder structure
    pass
