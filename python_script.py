import os
import subprocess

# Path to the Android SDK Emulator tools
ANDROID_SDK_PATH = "/path/to/android/sdk"  # Update this path
EMULATOR_NAME = "test_avd"  # The name of your AVD (Android Virtual Device)
APK_PATH = "/path/to/sample_app.apk"  # Update this with the path to your APK file


def start_emulator():
    """Starts the Android Emulator."""
    emulator_path = os.path.join(ANDROID_SDK_PATH, "emulator", "emulator")
    avd_path = os.path.join(ANDROID_SDK_PATH, "avd", EMULATOR_NAME)

    print("Starting the emulator...")
    process = subprocess.Popen(
        [emulator_path, "-avd", EMULATOR_NAME],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return process


def install_apk():
    """Installs an APK on the running emulator."""
    adb_path = os.path.join(ANDROID_SDK_PATH, "platform-tools", "adb")

    print("Installing APK...")
    result = subprocess.run(
        [adb_path, "install", APK_PATH],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if result.returncode == 0:
        print("APK installed successfully!")
    else:
        print("Failed to install APK:", result.stderr.decode())


def log_system_info():
    """Retrieves and logs system information from the emulator."""
    adb_path = os.path.join(ANDROID_SDK_PATH, "platform-tools", "adb")

    print("Fetching system information...")
    commands = [
        "shell getprop ro.build.version.release",  # OS version
        "shell getprop ro.product.model",  # Device model
        "shell cat /proc/meminfo"  # Memory info
    ]

    for command in commands:
        result = subprocess.run(
            [adb_path] + command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            print(command, ":\n", result.stdout.decode().strip())
        else:
            print("Failed to fetch:", command, result.stderr.decode())


if __name__ == "__main__":
    emulator_process = start_emulator()

    try:
        input("Press Enter once the emulator has started...")
        install_apk()
        log_system_info()
    finally:
        print("Stopping the emulator...")
        emulator_process.terminate()
