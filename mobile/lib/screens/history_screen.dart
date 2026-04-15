/// Diagnosis History Screen
///
/// Owner: Jeshik Neupane
///
/// Shows a list of past diagnoses stored locally.
///
/// TODO (Jeshik):
///   - Load diagnosis history from shared_preferences
///   - Display as scrollable list with DiagnosisCard widgets
///   - Allow tapping to view full details
///   - Add clear history option

import 'package:flutter/material.dart';

class HistoryScreen extends StatelessWidget {
  const HistoryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // TODO (Jeshik): Load and display diagnosis history
    return Scaffold(
      appBar: AppBar(title: const Text('History')),
      body: const Center(
        child: Text('History Screen — TODO (Jeshik)'),
      ),
    );
  }
}
