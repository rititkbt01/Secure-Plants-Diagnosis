/// Diagnosis Result Model
///
/// Owner: Jeshik Neupane
///
/// Represents the full response from POST /api/v1/diagnose.
/// Maps JSON response to a Dart data class.
///
/// TODO (Jeshik):
///   - Add all fields matching the DiagnosisResponse schema
///   - Implement fromJson() constructor
///   - Implement toJson() method

class DiagnosisResult {
  final String diseaseName;
  final double confidence;
  final String crop;
  final String diseaseClass;
  final bool isHealthy;
  final Treatment treatment;
  final int inferenceTimeMs;
  final DateTime timestamp;

  const DiagnosisResult({
    required this.diseaseName,
    required this.confidence,
    required this.crop,
    required this.diseaseClass,
    required this.isHealthy,
    required this.treatment,
    required this.inferenceTimeMs,
    required this.timestamp,
  });

  /// TODO (Jeshik): Implement fromJson factory constructor
  factory DiagnosisResult.fromJson(Map<String, dynamic> json) {
    // TODO: Parse JSON fields
    throw UnimplementedError('fromJson not implemented yet');
  }

  /// TODO (Jeshik): Implement toJson method
  Map<String, dynamic> toJson() {
    // TODO: Serialize to JSON
    throw UnimplementedError('toJson not implemented yet');
  }
}
