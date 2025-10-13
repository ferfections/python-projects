import socket
import json
from user import User

HOST = '127.0.0.1'
PORT = 9999

def save_user_to_json(user):
    """Guarda el usuario en users.json (agregando sin borrar los anteriores)."""
    filename = "users.json"

    try:
        with open(filename, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    users.append(user.to_dict())

    with open(filename, "w") as file:
        json.dump(users, file, indent=4)

    print(f"Usuario {user.username} guardado correctamente ✅")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        print(f"Conexión recibida de {addr}")

        data = conn.recv(1024).decode("utf-8")
        if not data:
            break

        user_data = json.loads(data)  # Recibimos un JSON del cliente
        user = User(**user_data)

        print(f"Usuario recibido: {user}")
        save_user_to_json(user)

        conn.send("Usuario recibido y guardado correctamente.".encode("utf-8"))
        conn.close()

if __name__ == "__main__":
    main()