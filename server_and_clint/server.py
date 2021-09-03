import socket
import sys

# get host name from command line argument
# host = sys.argv[1]
# host = socket.gethostbyname(socket.gethostname())
port = int(sys.argv[1])
# port = 9999

# create a socket object. Here AF(Address Family)_INET(Internet) = IPv4, STREAM = TCP  // and also we can use SOCK_DGRAM = UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostbyname(socket.gethostname()), port))
sock.listen(3)

# wait for a connection
print("\nWaiting for a connection\n")
conn, addr = sock.accept()

# receive data from client
print(f"\nConnection established with: {str(addr)}")
# message = "\nWelcome to the server\n"
# conn.send(message.encode("ascii"))
# conn.close()

while True:
    # receive msg from client
    data = conn.recv(1024)
    if data == b"exit":
        break
    print(f"Client: {str(data.decode())}")
    
    # send msg to client
    msg = input("Server: -> ")
    conn.send(msg.encode('ascii'))
    if msg == "exit":
        break
conn.close()

