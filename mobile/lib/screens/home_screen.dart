/// Home Screen
///
/// Owner: Jeshik Neupane
///
/// Main landing screen after login.
/// Shows quick diagnosis button and recent diagnosis history.
///
/// TODO (Jeshik):
///   - Design layout with diagnose button and recent history list
///   - Show app logo and brief instruction text
///   - Navigate to CameraScreen on diagnose button tap
///   - Show last 3 diagnoses from local storage

import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // TODO (Jeshik): Implement home screen UI
    return Scaffold(
      appBar: AppBar(title: const Text('Secure-Plants Diagnosis')),
      body: const Center(
        child: Text('Home Screen — TODO (Jeshik)'),
      ),
      // TODO (Jeshik): Add FAB or button to navigate to CameraScreen
    );
  }
}
