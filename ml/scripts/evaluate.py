"""
Model Evaluation Script
========================
Owner: Rishav Dhakal (Model Optimization Lead)

Evaluates trained DeiT-Tiny and ResNet-50 models on held-out test set.
Generates comparison report and plots.

Usage:
    python ml/scripts/evaluate.py --model student
    python ml/scripts/evaluate.py --model teacher
    python ml/scripts/evaluate.py --model both  # Generate comparison

Output:
    Accuracy, Precision, Recall, F1-Score per class
    Confusion matrix plot
    Model comparison chart

TODO (Rishav):
    - Load model from checkpoint
    - Run evaluate_model() from metrics.py
    - Generate and save all plots
    - Print metrics table
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))


def main():
    """
    TODO (Rishav): Implement evaluation script
    """
    print("Model Evaluation")
    print("=" * 50)
    print("TODO (Rishav): Implement evaluation pipeline")


if __name__ == "__main__":
    main()
