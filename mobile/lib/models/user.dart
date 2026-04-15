/// User Model
///
/// Owner: Jeshik Neupane
///
/// Represents an authenticated user with JWT tokens.
///
/// TODO (Jeshik):
///   - Implement fromJson() constructor
///   - Add token validation helper (isTokenExpired)

class User {
  final String userId;
  final String username;
  final String email;
  final String accessToken;
  final String refreshToken;

  const User({
    required this.userId,
    required this.username,
    required this.email,
    required this.accessToken,
    required this.refreshToken,
  });

  /// TODO (Jeshik): Implement fromJson factory constructor
  factory User.fromJson(Map<String, dynamic> json) {
    throw UnimplementedError('fromJson not implemented yet');
  }
}
