import socket 

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
mySocket.connect(('duckduckgo.com', 80));

cmd = 'GET https://google.com HTTP/1.0\n\n'.encode();
mySocket.send(cmd)

while True:
    data = mySocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mySocket.close();
