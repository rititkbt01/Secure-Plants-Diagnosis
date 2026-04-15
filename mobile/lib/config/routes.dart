/// App Navigation Routes
///
/// Owner: Jeshik Neupane
///
/// Defines named routes for all screens.
///
/// TODO (Jeshik):
///   - Define all route constants
///   - Map routes to screen widgets

import 'package:flutter/material.dart';
// import '../screens/home_screen.dart';
// import '../screens/camera_screen.dart';
// import '../screens/diagnosis_screen.dart';
// import '../screens/history_screen.dart';
// import '../screens/auth/login_screen.dart';
// import '../screens/auth/register_screen.dart';

class AppRoutes {
  static const String login = '/login';
  static const String register = '/register';
  static const String home = '/home';
  static const String camera = '/camera';
  static const String diagnosis = '/diagnosis';
  static const String history = '/history';

  // TODO (Jeshik): Map route names to screen widgets
  static Map<String, WidgetBuilder> get routes => {
    // login: (_) => const LoginScreen(),
    // register: (_) => const RegisterScreen(),
    // home: (_) => const HomeScreen(),
    // camera: (_) => const CameraScreen(),
    // history: (_) => const HistoryScreen(),
  };
}
