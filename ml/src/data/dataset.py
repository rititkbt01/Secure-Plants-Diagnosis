"""
Custom PyTorch Dataset — PlantVillage
======================================
Owner: Rishi Kumar Kushwaha (Data Engineering Lead)

Custom Dataset class for loading the PlantVillage dataset,
filtered to our 15 disease classes (3 crops: tomato, potato, bell pepper).

PlantVillage Structure:
    data/raw/PlantVillage/
        Tomato___Early_blight/
            image001.jpg
            ...
        Tomato___Late_blight/
            ...
        Potato___Early_Blight/
            ...

TODO (Rishi):
    - Implement PlantVillageDataset class
    - Implement class-to-index mapping (15 classes)
    - Implement folder-name-to-disease-class mapping
    - Apply transforms during __getitem__
    - Handle corrupt images gracefully
"""

import os
from pathlib import Path
# from PIL import Image
# from torch.utils.data import Dataset
# from torchvision import transforms


# Mapping: PlantVillage folder name → our disease_class string
# (PlantVillage uses format: Crop___Disease_name)
FOLDER_TO_CLASS = {
    "Tomato___Bacterial_spot":          "tomato_bacterial_spot",
    "Tomato___Early_blight":            "tomato_early_blight",
    "Tomato___Late_blight":             "tomato_late_blight",
    "Tomato___Leaf_Mold":               "tomato_leaf_mold",
    "Tomato___Septoria_leaf_spot":      "tomato_septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite": "tomato_spider_mites",
    "Tomato___Target_Spot":             "tomato_target_spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "tomato_yellow_leaf_curl_virus",
    "Tomato___Tomato_mosaic_virus":     "tomato_mosaic_virus",
    "Tomato___healthy":                 "tomato_healthy",
    "Potato___Early_Blight":            "potato_early_blight",
    "Potato___Late_blight":             "potato_late_blight",
    "Potato___healthy":                 "potato_healthy",
    "Pepper,_bell___Bacterial_spot":    "pepper_bacterial_spot",
    "Pepper,_bell___healthy":           "pepper_healthy",
}

# Class-to-index mapping (must match inference_service.py DISEASE_CLASSES)
CLASS_TO_IDX = {
    "tomato_bacterial_spot": 0,
    "tomato_early_blight": 1,
    "tomato_late_blight": 2,
    "tomato_leaf_mold": 3,
    "tomato_septoria_leaf_spot": 4,
    "tomato_spider_mites": 5,
    "tomato_target_spot": 6,
    "tomato_yellow_leaf_curl_virus": 7,
    "tomato_mosaic_virus": 8,
    "tomato_healthy": 9,
    "potato_early_blight": 10,
    "potato_late_blight": 11,
    "potato_healthy": 12,
    "pepper_bacterial_spot": 13,
    "pepper_healthy": 14,
}

NUM_CLASSES = 15


class PlantVillageDataset:
    """
    Custom Dataset for PlantVillage (filtered to 15 classes).

    Args:
        root_dir: Path to PlantVillage folder (containing class subfolders).
        transform: torchvision transforms to apply to each image.
        split: 'train', 'val', or 'test'.

    TODO (Rishi):
        - Implement __init__ to scan folders and collect image paths
        - Implement __len__ to return total number of images
        - Implement __getitem__ to load image, apply transform, return (tensor, label)
        - Filter only folders that are in FOLDER_TO_CLASS
    """

    def __init__(self, root_dir: str, transform=None, split: str = "train"):
        # TODO (Rishi): Scan root_dir, build self.samples list of (image_path, label_idx)
        pass

    def __len__(self) -> int:
        # TODO (Rishi): Return len(self.samples)
        pass

    def __getitem__(self, idx: int):
        """
        Return (image_tensor, label_index) for a given index.

        TODO (Rishi):
            - Load image from self.samples[idx][0] using PIL
            - Convert to RGB
            - Apply self.transform
            - Return (tensor, label_idx)
        """
        pass
