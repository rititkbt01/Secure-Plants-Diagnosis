/// Authentication Service — JWT Token Management
///
/// Owner: Jeshik Neupane
///
/// Manages user authentication state and JWT token lifecycle.
/// Tokens stored securely using flutter_secure_storage.
///
/// TODO (Jeshik):
///   - Implement login() — POST to /auth/login, store tokens
///   - Implement register() — POST to /auth/register
///   - Implement logout() — clear stored tokens
///   - Implement refreshToken() — use refresh token to get new access token
///   - Implement getAccessToken() — return stored access token
///   - Implement isLoggedIn() — check if valid token exists

// import 'package:flutter_secure_storage/flutter_secure_storage.dart';
// import '../config/app_config.dart';
// import '../models/user.dart';

class AuthService {
  // Storage keys
  static const String _accessTokenKey = 'access_token';
  static const String _refreshTokenKey = 'refresh_token';
  static const String _userIdKey = 'user_id';

  // TODO (Jeshik): Initialize flutter_secure_storage instance

  /// Login with username and password.
  ///
  /// On success: stores access and refresh tokens securely.
  /// On failure: throws AuthException with error message.
  ///
  /// TODO (Jeshik): Implement
  Future<dynamic> login(String username, String password) async {
    throw UnimplementedError('login() not implemented yet');
  }

  /// Register a new user account.
  ///
  /// TODO (Jeshik): Implement
  Future<void> register(String username, String email, String password) async {
    throw UnimplementedError('register() not implemented yet');
  }

  /// Get stored JWT access token.
  ///
  /// Returns null if not logged in.
  ///
  /// TODO (Jeshik): Read from flutter_secure_storage
  Future<String?> getAccessToken() async {
    // TODO (Jeshik): Implement
    return null;
  }

  /// Check if user is currently logged in (has valid token).
  ///
  /// TODO (Jeshik): Check if access token exists in storage
  Future<bool> isLoggedIn() async {
    // TODO (Jeshik): Implement
    return false;
  }

  /// Clear all stored tokens (logout).
  ///
  /// TODO (Jeshik): Delete all keys from flutter_secure_storage
  Future<void> logout() async {
    throw UnimplementedError('logout() not implemented yet');
  }
}
