import requests
import json
import platform
import uuid


# Function to collect mock data
def collect_device_info():
    # Mock device data (you can replace this with actual data in a real-world scenario)
    device_id = str(uuid.uuid4())  # Unique device identifier
    system_info = {
        'device_id': device_id,
        'system': platform.system(),  # e.g., 'Linux', 'Windows'
        'node': platform.node(),  # Machine name
        'release': platform.release(),  # OS release version
        'version': platform.version()  # OS version
    }
    return system_info


# Function to send data to the backend server
def send_data_to_backend(data, backend_url):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(backend_url, json=data, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print("Data sent successfully!")
            print("Server Response:", response.text)
        else:
            print(f"Error: Unable to send data. Status Code: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"Error while sending data: {e}")


# Main execution
if __name__ == "__main__":
    # Backend URL (replace with the actual URL of your backend server)
    backend_url = "http://your-backend-server.com/api/device-info"

    # Collect mock data
    data = collect_device_info()

    # Send data to the backend
    send_data_to_backend(data, backend_url)
