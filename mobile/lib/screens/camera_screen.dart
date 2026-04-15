/// Camera Screen
///
/// Owner: Jeshik Neupane
///
/// Allows user to capture or select a leaf image.
/// Provides visual guidance for good image quality.
/// Validates image before proceeding to diagnosis.
///
/// TODO (Jeshik):
///   - Add camera capture button with guidance overlay
///   - Show "Hold steady", "Add more light" guidance messages
///   - Compress image using ImageValidator before upload
///   - Navigate to DiagnosisScreen with captured image
///   - Show loading state during API call

import 'package:flutter/material.dart';

class CameraScreen extends StatefulWidget {
  const CameraScreen({super.key});

  @override
  State<CameraScreen> createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen> {
  // TODO (Jeshik): State variables for selected image, loading, error

  @override
  Widget build(BuildContext context) {
    // TODO (Jeshik): Implement camera/gallery UI with guidance
    return Scaffold(
      appBar: AppBar(title: const Text('Take a Photo')),
      body: const Center(
        child: Text('Camera Screen — TODO (Jeshik)'),
      ),
    );
  }
}
