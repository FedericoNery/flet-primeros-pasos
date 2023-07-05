import socket
import select
import threading

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345       # Puerto del servidor
BUFFER_SIZE = 1024  # Tamaño del búfer de recepción

# Lista de clientes y salas de chat
clients = []
rooms = {}

# Función para transmitir mensajes a todos los clientes en una sala de chat
def broadcast(message, room):
    for client in rooms[room]:
        client.send(message)

# Función de manejo de clientes
def handle_client(client, address):
    client.send("Ingrese el nombre de su sala de chat: ".encode())
    room = client.recv(BUFFER_SIZE).decode()

    # Verificar si la sala de chat ya existe, si no, crearla
    if room not in rooms:
        rooms[room] = []

    rooms[room].append(client)

    while True:
        try:
            message = client.recv(BUFFER_SIZE)
            if message:
                broadcast(message, room)
            else:
                # Si no se reciben datos, desconectar al cliente
                if client in rooms[room]:
                    rooms[room].remove(client)
                client.close()
                broadcast("{} se ha desconectado".format(address).encode(), room)
                break
        except:
            continue

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configurar el socket para reutilizar la dirección
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Vincular el socket a la dirección y puerto
server_socket.bind((HOST, PORT))

# Escuchar conexiones entrantes
server_socket.listen(10)
print('El servidor está escuchando en {}:{}'.format(HOST, PORT))

while True:
    # Aceptar nuevas conexiones
    client_socket, client_address = server_socket.accept()

    # Agregar el cliente a la lista de clientes
    clients.append(client_socket)

    # Crear un hilo para manejar al cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

# Cerrar la conexión del servidor
server_socket.close()