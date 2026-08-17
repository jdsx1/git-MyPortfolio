import subprocess
import platform
from datetime import datetime


# Devices we want to test
devices = {
    "Local Gateway": "192.168.1.1",
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1"
}


def ping_device(ip_address):

    # Windows uses -n
    # Linux / Mac use -c
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    command = [
        "ping",
        parameter,
        "1",
        ip_address
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


print("--------------------------------------")
print("     JDS NETWORK HEALTH CHECKER")
print("--------------------------------------")

print(f"Scan started: {datetime.now()}")
print()


for device_name, ip in devices.items():

    if ping_device(ip):

        print(
            f"[ONLINE]  {device_name:15} {ip}"
        )

    else:

        print(
            f"[OFFLINE] {device_name:15} {ip}"
        )


print()
print("Network scan completed.")