from cryptography.fernet import Fernet

def main():
    print("Módulo de criptografía")

    mensaje = "Este es el mensaje super secreto"

    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(bytes(mensaje, 'utf-8'))

    print(f.decrypt(token))
    

    
if __name__ == "__main__":
    main()
