/// App-wide Constants
///
/// Owner: Jeshik Neupane

class AppConstants {
  // Disease class display names (maps backend disease_class to human-readable)
  static const Map<String, String> diseaseDisplayNames = {
    'tomato_bacterial_spot': 'Tomato Bacterial Spot',
    'tomato_early_blight': 'Tomato Early Blight',
    'tomato_late_blight': 'Tomato Late Blight',
    'tomato_leaf_mold': 'Tomato Leaf Mold',
    'tomato_septoria_leaf_spot': 'Tomato Septoria Leaf Spot',
    'tomato_spider_mites': 'Tomato Spider Mites',
    'tomato_target_spot': 'Tomato Target Spot',
    'tomato_yellow_leaf_curl_virus': 'Tomato Yellow Leaf Curl Virus',
    'tomato_mosaic_virus': 'Tomato Mosaic Virus',
    'tomato_healthy': 'Healthy Tomato',
    'potato_early_blight': 'Potato Early Blight',
    'potato_late_blight': 'Potato Late Blight',
    'potato_healthy': 'Healthy Potato',
    'pepper_bacterial_spot': 'Bell Pepper Bacterial Spot',
    'pepper_healthy': 'Healthy Bell Pepper',
  };

  // Error messages
  static const String errorNetworkTimeout = 'Connection timeout. Please check your internet connection.';
  static const String errorFileTooLarge = 'Image is too large. Please use an image under 5MB.';
  static const String errorInvalidFile = 'Invalid file type. Please use a JPEG or PNG image.';
  static const String errorUnauthorized = 'Session expired. Please log in again.';
  static const String errorRateLimit = 'Too many requests. Please wait a moment and try again.';
  static const String errorServerError = 'Server error. Please try again later.';
  static const String warningLowConfidence = 'Low confidence diagnosis. We recommend consulting an agricultural expert.';
}
