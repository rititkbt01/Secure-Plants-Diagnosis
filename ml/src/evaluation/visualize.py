"""
Visualization Utilities
========================
Owner: Rishav Dhakal (Model Optimization Lead)

Generates plots for evaluation results:
    - Confusion matrix heatmap
    - Training/validation loss curves
    - Per-class accuracy bar chart
    - Confidence distribution histogram
    - DeiT vs ResNet-50 comparison chart

TODO (Rishav):
    - Implement plot_confusion_matrix()
    - Implement plot_training_curves()
    - Implement plot_per_class_accuracy()
    - Implement plot_model_comparison()
    - Save plots to ml/reports/figures/ folder
"""

# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np


def plot_confusion_matrix(cm, class_names: list, save_path: str = None):
    """
    Plot confusion matrix heatmap.

    Args:
        cm: Confusion matrix array from sklearn.
        class_names: List of disease class names.
        save_path: If provided, save figure to this path.

    TODO (Rishav): Use seaborn.heatmap, annotate cells, save figure
    """
    pass


def plot_training_curves(history: dict, save_path: str = None):
    """
    Plot training and validation loss/accuracy curves.

    Args:
        history: {'train_loss': [...], 'val_loss': [...], 'train_acc': [...], 'val_acc': [...]}
        save_path: If provided, save figure to this path.

    TODO (Rishav): Plot dual y-axis (loss + accuracy) per epoch
    """
    pass


def plot_model_comparison(deit_metrics: dict, resnet_metrics: dict, save_path: str = None):
    """
    Create comparison bar chart: DeiT-Tiny vs ResNet-50.

    Metrics to compare: Accuracy, Precision, Recall, F1-Score, Inference Time.

    TODO (Rishav): Generate grouped bar chart comparing both models
    """
    pass
