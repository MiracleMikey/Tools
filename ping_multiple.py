""" Script to ping multiple ips """

import platform
import os 

for octet in range(254):
    # assign ip class as needed
    ip = "192.168.0.{0}".format(octet + 1)
    # determine current os
    current_os = platform.system().lower()
    #craft ping command based on OS
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 1 {ip} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 1 {ip} > /dev/null 2>&1"
    #run command and capture exit code 
    exit_code = os.system(ping_cmd)
    # if host is up print the ip address
    if exit_code == 0:
        print(f"Host up: {ip} ")
