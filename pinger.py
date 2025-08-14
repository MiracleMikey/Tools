import platform
import os

#assign ip address 
ip = "192.168.0.1"

# Determine current running OS
current_os = platform.system().lower()

if current_os == "windows":
    ping_command = f"ping -n 1 -w 2 {ip} > nul"
else:
    ping_command = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    
# Print command output to the console
exit_code = os.system(ping_command)
print(exit_code)
