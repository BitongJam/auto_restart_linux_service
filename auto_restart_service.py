import subprocess
import time

def check_and_restart_service(service_name):
    while True:
        try:
            # Check service status using systemctl
            status = subprocess.run(['systemctl', 'is-active', '--quiet', service_name]).returncode

            if status != 0:
                print(f"Service '{service_name}' is not running. Restarting...")
                subprocess.run(['sudo', 'systemctl', 'restart', service_name], check=True)
                print(f"Service '{service_name}' restarted successfully.")
            else:
                print(f"Service '{service_name}' is running.")

            # Wait for a period before checking again (e.g., every 10 seconds)
            time.sleep(10)

        except subprocess.CalledProcessError as e:
            print(f"Failed to check or restart service '{service_name}'. Error: {e}")

# Example usage:
if __name__ == "__main__":
    service_name = 'jargonV11'
    check_and_restart_service(service_name)
