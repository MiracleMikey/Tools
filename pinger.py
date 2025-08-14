import platform
import os

#assign ip address 
ip = "192.168.0.111"

# Determine current running OS
current_os = platform.system().lower()

if current_os == "windows":
    ping_command = f"ping -n 1 -w 2 {ip} > nul"
else:
    ping_command = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"


exit_code = os.system(ping_command)
if exit_code == 0:
    print("The host is up")
else:
    print("No response")

