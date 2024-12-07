# servidor.py
import socket

def iniciar_servidor():
    # 1. Crear un socket
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Asociar el socket con una IP y un puerto
    servidor_socket.bind(('127.0.0.1', 12345))  # Dirección IP localhost, puerto 12345
    
    # 3. Escuchar por conexiones entrantes
    servidor_socket.listen(1)  # Número máximo de conexiones simultáneas
    
    print("Servidor escuchando en el puerto 12345...")
    
    while True:
        # 4. Aceptar una conexión
        cliente_socket, direccion_cliente = servidor_socket.accept()
        print(f"Conexión establecida con: {direccion_cliente}")
        
        # 5. Recibir un mensaje del cliente
        mensaje_cliente = cliente_socket.recv(1024).decode('utf-8')
        print(f"Recibido: {mensaje_cliente}")
        
        # 6. Responder al cliente
        respuesta = "Mensaje recibido"
        cliente_socket.send(respuesta.encode('utf-8'))
        
        # 7. Cerrar la conexión
        cliente_socket.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    iniciar_servidor()