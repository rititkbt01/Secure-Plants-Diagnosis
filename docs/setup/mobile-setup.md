# Mobile Setup Guide (Flutter)

**Owner:** Jeshik Neupane (App Development Lead)

---

## Prerequisites

1. Flutter SDK 3.x (stable channel): https://docs.flutter.dev/get-started/install
2. Android Studio (for Android emulator) or Xcode (for iOS simulator, macOS only)
3. A physical Android/iOS device OR configured emulator

Verify installation:
```bash
flutter doctor
```
All checkboxes should be green (or yellow with notes).

---

## Project Structure

```
mobile/lib/
├── main.dart          ← App entry point
├── app.dart           ← MaterialApp, theme, routes
├── config/            ← API base URL, theme, routes
├── models/            ← Data models (DiagnosisResult, Treatment, User)
├── screens/           ← UI screens (home, camera, diagnosis, history, auth)
├── services/          ← API calls, auth, camera, validation
├── widgets/           ← Reusable UI components
└── utils/             ← Constants, helper functions
```

---

## Installation

```bash
cd mobile
flutter pub get
```

---

## Configuration

Update `mobile/lib/config/app_config.dart`:
```dart
// Change baseUrl to your backend URL
static const String baseUrl = 'http://localhost:8000/api/v1';
// For Android emulator: 'http://10.0.2.2:8000/api/v1'
// For physical device: 'http://YOUR_MACHINE_IP:8000/api/v1'
```

---

## Running the App

```bash
# List available devices
flutter devices

# Run on specific device
flutter run -d <device_id>

# Run on Chrome (web — for UI prototyping)
flutter run -d chrome
```

---

## Key Dependencies (pubspec.yaml)

| Package | Purpose |
|---------|---------|
| `http` | HTTP requests to backend |
| `camera` | Device camera access |
| `image_picker` | Pick image from gallery or camera |
| `flutter_secure_storage` | Secure JWT token storage |
| `shared_preferences` | Local app preferences |
| `provider` | State management |
| `image` | Image manipulation/compression |
| `intl` | Date/time formatting |

---

## Running Flutter Tests

```bash
cd mobile
flutter test
flutter test --coverage  # With coverage
```
