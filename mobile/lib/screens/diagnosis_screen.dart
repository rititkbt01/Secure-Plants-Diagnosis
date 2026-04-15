/// Diagnosis Result Screen
///
/// Owner: Jeshik Neupane
///
/// Displays the diagnosis result from the backend:
///   - Disease name and crop type
///   - Confidence score with visual progress bar
///   - Expert-verified treatment details
///   - Warning if confidence < 60% (suggest expert verification)
///
/// TODO (Jeshik):
///   - Display DiagnosisResult data from navigation arguments
///   - Show ConfidenceIndicator widget with color coding
///   - Show TreatmentCard widget with collapsible sections
///   - Add "Save to History" button
///   - Add "New Diagnosis" button

import 'package:flutter/material.dart';
// import '../models/diagnosis_result.dart';
// import '../widgets/confidence_indicator.dart';
// import '../widgets/treatment_card.dart';

class DiagnosisScreen extends StatelessWidget {
  const DiagnosisScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // TODO (Jeshik): Receive DiagnosisResult from navigation args
    // final result = ModalRoute.of(context)!.settings.arguments as DiagnosisResult;

    return Scaffold(
      appBar: AppBar(title: const Text('Diagnosis Result')),
      body: const Center(
        child: Text('Diagnosis Result Screen — TODO (Jeshik)'),
      ),
    );
  }
}
