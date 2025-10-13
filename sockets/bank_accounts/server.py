from bankAccount import BankAccount
import socket
import json

HOST = '127.0.0.1'
PORT = 9999
addr = (HOST, PORT)

def store_JSON(bankAccount: BankAccount):
    filename = "accounts.json"

    try:
        with open(filename, "r") as file:
            accounts = json.load(file)
    except FileNotFoundError:
        users = []

    accounts.append(bankAccount.toDict())

    print("Cuenta bancaria guardada correctamente")

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
        bankAccount = BankAccount(**user_data)

        store_JSON(bankAccount)
        conn.close()

