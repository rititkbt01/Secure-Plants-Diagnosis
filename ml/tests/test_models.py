"""
Model Architecture Tests
==========================
Owner: Yashraj Shrestha

Tests for model architecture and forward pass:
    - test_teacher_model_output_shape
    - test_student_model_output_shape
    - test_distillation_loss_computation
    - test_model_loads_from_checkpoint

TODO (Yashraj):
    - Implement all test cases
    - These are unit tests (fast — no actual training)
"""

import pytest


class TestTeacherModel:
    """Test suite for ResNet-50 teacher model."""

    def test_teacher_output_shape(self):
        """
        Test ResNet-50 outputs (batch_size, 15) tensor.

        TODO (Yashraj): Create model, run forward pass with random input
        """
        pass


class TestStudentModel:
    """Test suite for DeiT-Tiny student model."""

    def test_student_output_shape(self):
        """
        Test DeiT-Tiny outputs (batch_size, 15) tensor.

        TODO (Yashraj): Create model, run forward pass with random input
        """
        pass

    def test_distillation_loss_computation(self):
        """
        Test DistillationLoss computes without errors.

        TODO (Yashraj): Create random logits + soft labels, compute loss
        """
        pass
