# cliente.py
import socket

def conectar_a_servidor():
    # 1. Crear un socket
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Conectarse al servidor (IP y puerto donde el servidor está escuchando)
    cliente_socket.connect(('127.0.0.1', 12345))  # Dirección IP localhost, puerto 12345
    
    # 3. Enviar un mensaje al servidor
    mensaje = "Hola, desde el cliente."
    cliente_socket.send(mensaje.encode('utf-8'))
    
    # 4. Esperar una respuesta del servidor
    respuesta = cliente_socket.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {respuesta}")
    
    # 5. Cerrar la conexión
    cliente_socket.close()
    print("Conexión cerrada.")

if __name__ == "__main__":
    conectar_a_servidor()