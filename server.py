import socket

# Creamos un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignamos una dirección y puerto al socket
server_address = ('', 12345)  # '' indica que escucharemos en todas las interfaces de red
server_socket.bind(server_address)

# Escuchamos conexiones entrantes
server_socket.listen(1)

print("Esperando conexión en el puerto", server_address[1])

while True:
    # Esperamos por una conexión
    client_socket, client_address = server_socket.accept()

    try:
        print("Conexión desde", client_address)

        # Recibimos los datos del cliente
        data = client_socket.recv(1024)
        print("Mensaje recibido:", data.decode())

    finally:
        # Cerramos la conexión
        client_socket.close()
