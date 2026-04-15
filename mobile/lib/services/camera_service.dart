/// Camera Service — Image Capture
///
/// Owner: Jeshik Neupane
///
/// Handles camera capture and gallery image selection.
/// Provides guidance for good image quality (lighting, focus, framing).
///
/// TODO (Jeshik):
///   - Implement captureFromCamera() using image_picker
///   - Implement pickFromGallery() using image_picker
///   - Add real-time brightness check before allowing capture
///   - Show guidance overlay: "Hold steady", "Move closer", "Add more light"

import 'dart:io';
// import 'package:image_picker/image_picker.dart';

class CameraService {
  // TODO (Jeshik): Initialize ImagePicker instance

  /// Capture image using device camera.
  ///
  /// Returns File on success, null if user cancelled.
  ///
  /// TODO (Jeshik):
  ///   - Use ImagePicker.pickImage(source: ImageSource.camera)
  ///   - Set imageQuality: AppConfig.imageQuality (85)
  ///   - Return File from XFile.path
  Future<File?> captureFromCamera() async {
    // TODO (Jeshik): Implement
    return null;
  }

  /// Pick image from device gallery.
  ///
  /// TODO (Jeshik): Use ImagePicker.pickImage(source: ImageSource.gallery)
  Future<File?> pickFromGallery() async {
    // TODO (Jeshik): Implement
    return null;
  }
}
