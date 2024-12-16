# Virtual Android System Simulation

This project simulates a virtual Android environment, installs a sample app, and retrieves system information.

## Prerequisites
1. **Android SDK**: Download and install the Android SDK from [developer.android.com](https://developer.android.com/studio).
2. **Android Virtual Device (AVD)**: Create an AVD using Android Studio or the `avdmanager` tool.
3. **Python Environment**: Python 3.x and required libraries.

## Setup Instructions

1. Update the following variables in the script:
   - `ANDROID_SDK_PATH`: Path to your Android SDK.
   - `APK_PATH`: Path to the APK file you want to install.
   - `EMULATOR_NAME`: Name of the AVD.

2. Make sure the `adb` and `emulator` tools are accessible. These are part of the Android SDK.

## Running the Script

1. Launch the script:
   ```bash
   python virtual_android.py
