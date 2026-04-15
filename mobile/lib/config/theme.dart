/// App Theme Configuration
///
/// Owner: Jeshik Neupane
///
/// Defines the visual theme — green color scheme (agriculture-appropriate).
///
/// TODO (Jeshik):
///   - Define primary color (green)
///   - Define text styles
///   - Define card and button styles

import 'package:flutter/material.dart';

class AppTheme {
  // Color Palette — Agriculture-inspired greens
  static const Color primaryGreen = Color(0xFF2E7D32);      // Dark green
  static const Color lightGreen = Color(0xFF66BB6A);        // Light green
  static const Color accentAmber = Color(0xFFFFA726);       // Warning/confidence
  static const Color errorRed = Color(0xFFD32F2F);          // Errors
  static const Color backgroundLight = Color(0xFFF1F8E9);   // Light green background

  // TODO (Jeshik): Define lightTheme ThemeData
  static ThemeData get lightTheme => ThemeData(
    // TODO: Configure full theme
    primaryColor: primaryGreen,
    colorScheme: ColorScheme.fromSeed(seedColor: primaryGreen),
    useMaterial3: true,
  );
}
