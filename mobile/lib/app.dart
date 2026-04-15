/// Application Root Widget
///
/// Owner: Jeshik Neupane
///
/// Configures MaterialApp with theme, routes, and initial screen.
///
/// TODO (Jeshik):
///   - Define app theme (green color scheme for agriculture)
///   - Define named routes for all screens
///   - Set initial route (login if not authenticated, home if authenticated)

import 'package:flutter/material.dart';
// import 'config/routes.dart';
// import 'config/theme.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    // TODO (Jeshik): Configure MaterialApp with theme and routes
    return MaterialApp(
      title: 'Secure-Plants Diagnosis',
      debugShowCheckedModeBanner: false,
      // theme: AppTheme.lightTheme,
      // initialRoute: AppRoutes.login,
      // routes: AppRoutes.routes,
    );
  }
}
