/// Application Configuration
///
/// Owner: Jeshik Neupane
///
/// Central configuration for the Flutter app.
/// Update baseUrl to point to your backend server.
///
/// TODO (Jeshik):
///   - Set correct baseUrl for development/production

class AppConfig {
  // ── Backend API ─────────────────────────────────────────────────
  /// Development: localhost for web, 10.0.2.2 for Android emulator
  static const String baseUrl = 'http://localhost:8000/api/v1';
  // For Android emulator: 'http://10.0.2.2:8000/api/v1'
  // For physical device: 'http://YOUR_MACHINE_IP:8000/api/v1'

  // ── API Timeouts ────────────────────────────────────────────────
  static const int connectTimeoutSeconds = 10;
  static const int receiveTimeoutSeconds = 30;  // Model inference can take up to 3s

  // ── Image Constraints ───────────────────────────────────────────
  static const int maxImageSizeBytes = 5 * 1024 * 1024;  // 5MB
  static const int targetImageSizeBytes = 300 * 1024;    // 300KB (compress to this)
  static const int imageQuality = 85;                    // JPEG quality

  // ── Confidence Threshold ────────────────────────────────────────
  /// Below this confidence, show "Low confidence — seek expert advice"
  static const double lowConfidenceThreshold = 0.60;

  // ── App Info ────────────────────────────────────────────────────
  static const String appName = 'Secure-Plants Diagnosis';
  static const String appVersion = '1.0.0';
}
