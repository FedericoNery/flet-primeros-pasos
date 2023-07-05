import socket
import threading

# Función para recibir mensajes del servidor
def receive_messages():
    while True:
        try:
            message = client_socket.recv(BUFFER_SIZE).decode()
            print(message)
        except:
            # Si ocurre un error, desconectar al cliente
            print("Ha ocurrido un error. Desconectando...")
            client_socket.close()
            break

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 12345       # Puerto del servidor
BUFFER_SIZE = 1024  # Tamaño del búfer de recepción

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor
client_socket.connect((HOST, PORT))
print('Conectado al servidor en {}:{}'.format(HOST, PORT))

# Iniciar un hilo para recibir mensajes del servidor
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Enviar mensajes al servidor
while True:
    message = input()
    client_socket.send(message.encode())

# Cerrar la conexión del cliente
client_socket.close()