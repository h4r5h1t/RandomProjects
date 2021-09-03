import socket
import sys


port = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostbyname(socket.gethostname()), port))

while True:
    # send a message to the server
    msg = input("Client: -> ")
    sock.send(msg.encode())
    if msg == "exit":
        break

    # receive a message from the server
    data = sock.recv(1024)
    print(f"Server: {str(data.decode())}")
    print(data.decode())
    if data == b"exit":
        break
sock.close()
