/// Helper Utilities
///
/// Owner: Jeshik Neupane
///
/// TODO (Jeshik):
///   - Implement formatConfidence() — 0.923 → "92.3%"
///   - Implement formatDate() — DateTime to readable string
///   - Implement getConfidenceColor() — Color based on confidence level

import 'package:flutter/material.dart';

/// Format confidence value as percentage string.
/// Example: 0.923 → "92.3%"
String formatConfidence(double confidence) {
  // TODO (Jeshik): Implement
  return '${(confidence * 100).toStringAsFixed(1)}%';
}

/// Get color for confidence level.
/// Green ≥ 0.80, Amber 0.60-0.79, Red < 0.60
Color getConfidenceColor(double confidence) {
  // TODO (Jeshik): Implement with AppTheme colors
  if (confidence >= 0.80) return Colors.green;
  if (confidence >= 0.60) return Colors.amber;
  return Colors.red;
}
