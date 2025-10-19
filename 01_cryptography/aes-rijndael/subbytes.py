import cryptography.fernet as fernet
from cryptography.utils import *

def main():
    key = fernet.Fernet.generate_key()
    print(f'Your key is {key}')
    f = fernet.Fernet(key)

    msg = "Hola Fernando"
    
    msg_encrypted = f.encrypt(msg.encode())
    print(f'The encripted code is {msg_encrypted}')
    print(f.decrypt(msg_encrypted))

if __name__ == "__main__":
    main()