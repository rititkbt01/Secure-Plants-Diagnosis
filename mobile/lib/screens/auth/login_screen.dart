/// Login Screen
///
/// Owner: Jeshik Neupane
///
/// User login with username and password.
/// On success: stores JWT tokens and navigates to HomeScreen.
///
/// TODO (Jeshik):
///   - Design login form with username + password fields
///   - Validate fields (non-empty, password min 8 chars)
///   - Call AuthService.login() on submit
///   - Show loading indicator during API call
///   - Handle 401 error with user-friendly message
///   - Navigate to HomeScreen on success
///   - Add "Register" link

import 'package:flutter/material.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  // TODO (Jeshik): Form controllers, loading state, error message

  @override
  Widget build(BuildContext context) {
    // TODO (Jeshik): Implement login form UI
    return Scaffold(
      appBar: AppBar(title: const Text('Login')),
      body: const Center(
        child: Text('Login Screen — TODO (Jeshik)'),
      ),
    );
  }
}
