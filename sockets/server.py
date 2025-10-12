import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('0.0.0.0', 9999)

server.listen(5) # 5 conexiones como máximo a la vez
print("Servidor escuchando en el puerto ", addr[1])

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    client.send("Hola desde el servidor".encode())