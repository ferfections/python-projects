from cryptography.fernet import Fernet
from json import load, dumps
import json



class Client:
    def __init__(self):
        self.username = None
        self.password = None

class CentralApp:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        self.users = {}

    def usernameExists(self, username) -> bool:
        ...

    def storeClient(self, client):
        with json
    
    def register(self):

        print(">> [Register]")

        while True:
            username = input(">> Username: ")

            if self.usernameExists(username):
                print(">> This username already exists, please choose another one.")
            else:
                break

        password = input(">> Password: ")

        new_client = Client(username, self.f.encrypt(bytes(password)))









def main():

    while True:
        print(">> [Operation List]")
        print(">> 1 - Register")
        print(">> 2 - Login")
        op = input(">> (1 or 2): ")

        if op == "1":
            register()
        elif op == "2":
            ...
        else:
            print(">> Wrong operation. Try again.")
 

if __name__ == "__main__":
    main()
    