#!/bin/bash
# Run Flutter mobile app
cd "$(dirname "$0")/.."
echo "Starting Flutter app..."
cd mobile
flutter run "$@"
