/// API Service — Backend Communication
///
/// Owner: Jeshik Neupane (App Development Lead)
///
/// Handles all HTTP communication with the FastAPI backend.
/// Attaches JWT token to all authenticated requests.
/// Manages image upload with proper multipart/form-data encoding.
///
/// TODO (Jeshik):
///   - Implement diagnose() — POST image to /api/v1/diagnose
///   - Implement getTreatment() — GET /api/v1/treatment/{disease_class}
///   - Add JWT Bearer token to all request headers
///   - Handle HTTP error responses (401, 400, 413, 429, 500)
///   - Implement request timeout (connectTimeout: 10s, receiveTimeout: 30s)

import 'dart:io';
// import 'package:http/http.dart' as http;
// import '../config/app_config.dart';
// import '../models/diagnosis_result.dart';
// import '../models/treatment.dart';
// import 'auth_service.dart';

class ApiService {
  // TODO (Jeshik): Initialize HTTP client with base URL and timeouts

  /// Upload leaf image and receive diagnosis result.
  ///
  /// [imageFile]: The image file captured by the camera.
  ///
  /// Returns DiagnosisResult on success.
  /// Throws ApiException on HTTP errors.
  ///
  /// TODO (Jeshik):
  ///   - Compress image before upload (use image_validator.dart)
  ///   - Create multipart/form-data request
  ///   - Attach JWT token from AuthService
  ///   - POST to AppConfig.baseUrl + '/diagnose'
  ///   - Parse response JSON into DiagnosisResult
  ///   - Handle 401 (token expired → refresh), 413 (too large), 429 (rate limit)
  Future<dynamic> diagnose(File imageFile) async {
    // TODO (Jeshik): Implement
    throw UnimplementedError('diagnose() not implemented yet');
  }

  /// Retrieve treatment for a specific disease class.
  ///
  /// TODO (Jeshik): GET AppConfig.baseUrl + '/treatment/{diseaseClass}'
  Future<dynamic> getTreatment(String diseaseClass) async {
    // TODO (Jeshik): Implement
    throw UnimplementedError('getTreatment() not implemented yet');
  }

  /// Check backend health status.
  ///
  /// TODO (Jeshik): GET AppConfig.baseUrl + '/health' (no auth required)
  Future<Map<String, dynamic>> checkHealth() async {
    // TODO (Jeshik): Implement
    throw UnimplementedError('checkHealth() not implemented yet');
  }
}
