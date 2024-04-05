import socket

# this code shows how to open a socket connection and retrieve the data

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org", 80))
command = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysocket.send(command)

while True:
    data = mysocket.recv(512)  # ask up to 512 characters
    if len(data) < 1:
        break
    print(data.decode())
mysocket.close()
