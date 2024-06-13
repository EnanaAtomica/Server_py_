import socket

#conexion UDP
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#conexion TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.180.237', 12345)) 
s.send("Hola, servidor".encode())

response = s.recv(1024).decode()

print(response)