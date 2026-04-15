/// Register Screen
///
/// Owner: Jeshik Neupane
///
/// New user registration form.
///
/// TODO (Jeshik):
///   - Design registration form (username, email, password, confirm password)
///   - Validate all fields
///   - Call AuthService.register() on submit
///   - Navigate to LoginScreen on success

import 'package:flutter/material.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  @override
  Widget build(BuildContext context) {
    // TODO (Jeshik): Implement registration form UI
    return Scaffold(
      appBar: AppBar(title: const Text('Create Account')),
      body: const Center(
        child: Text('Register Screen — TODO (Jeshik)'),
      ),
    );
  }
}
