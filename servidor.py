import socket 

ip = '192.168.180.237'
puerto = 2200

#conexion TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, puerto))
print(f"escuchando en el ip: {ip}, puerto: {puerto}")
s.listen()

conn, addr = s.accept()
data = conn.recv (1024)

conn.sendall("Message for client".encode())

print(data)

s.close()
#conexion UDP
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('localhost',12345))


# data, addr = s.recvfrom (1024)

# s.sendto("Message for client".encode(),addr)

# print("programa funca")
# print(data)
# s.close()