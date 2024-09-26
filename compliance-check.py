import os
import socket
import subprocess
import psutil

# Function to check password policy (Linux Example)
def check_password_policy():
    print("\nChecking Password Policy...")
    try:
        with open("/etc/login.defs", "r") as f:
            data = f.readlines()
            min_length = None
            max_days = None
            for line in data:
                if "PASS_MIN_LEN" in line:
                    min_length = int(line.split()[1])
                if "PASS_MAX_DAYS" in line:
                    max_days = int(line.split()[1])
            print(f"Minimum password length: {min_length}")
            print(f"Maximum password age (days): {max_days}")

            if min_length >= 8 and max_days <= 90:
                print("Password policy is compliant.")
            else:
                print("Password policy is non-compliant.")
    except Exception as e:
        print(f"Error checking password policy: {e}")

# Function to check if the OS is up to date (Linux Example using APT)
def check_patch_management():
    print("\nChecking Patch Management...")
    try:
        result = subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True)
        if "All packages are up to date" in result.stdout:
            print("Patch management is compliant.")
        else:
            print("System requires updates.")
    except Exception as e:
        print(f"Error checking patch management: {e}")

# Function to check if firewall is enabled
def check_firewall_status():
    print("\nChecking Firewall Status...")
    try:
        result = subprocess.run(["sudo", "ufw", "status"], capture_output=True, text=True)
        if "active" in result.stdout:
            print("Firewall is enabled.")
        else:
            print("Firewall is disabled.")
    except Exception as e:
        print(f"Error checking firewall status: {e}")

# Function to scan for open ports
def check_open_ports():
    print("\nChecking for Open Ports...")
    open_ports = []
    common_ports = [21, 22, 23, 25, 80, 443, 3389]

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex(('127.0.0.1', port))  # Scan localhost
        if result == 0:
            open_ports.append(port)
        sock.close()

    if open_ports:
        print(f"Open ports detected: {', '.join(map(str, open_ports))}. Please close unnecessary ports.")
    else:
        print("No open ports detected.")

# Function to check system health (e.g., CPU, RAM usage)
def check_system_health():
    print("\nChecking System Health...")
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_info.percent}%")

    if cpu_usage < 80 and memory_info.percent < 80:
        print("System health is compliant.")
    else:
        print("System is under high load.")

# Run the Compliance Checks
if __name__ == "__main__":
    print("Automated Security Compliance Checklist")
    check_password_policy()
    check_patch_management()
    check_firewall_status()
    check_open_ports()
    check_system_health()
