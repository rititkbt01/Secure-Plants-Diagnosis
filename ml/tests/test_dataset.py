"""
Dataset Tests
==============
Owner: Rishi Kumar Kushwaha

Tests for data loading and augmentation:
    - test_plantvillage_loads_correct_classes
    - test_image_tensor_shape
    - test_train_val_split_sizes
    - test_augmentation_produces_different_tensors
    - test_normalization_values

TODO (Rishi):
    - Implement all test cases
    - Use a small subset of dataset for tests (not full 54k images)
"""

import pytest


class TestPlantVillageDataset:
    """Test suite for PlantVillageDataset."""

    def test_dataset_loads_correct_number_of_classes(self):
        """
        Test dataset contains exactly 15 classes.

        TODO (Rishi): Load dataset, assert len(dataset.classes) == 15
        """
        pass

    def test_image_tensor_shape(self):
        """
        Test that loaded image has correct shape (3, 224, 224).

        TODO (Rishi): Load one sample, assert tensor.shape == (3, 224, 224)
        """
        pass

    def test_train_val_test_split_ratios(self):
        """
        Test that splits have approximately correct sizes.

        TODO (Rishi): Create splits, verify sizes are ~70/15/15%
        """
        pass
