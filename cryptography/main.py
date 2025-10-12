from cryptography.fernet import Fernet

def encriptar(mensaje: bytes, llave):
    f = Fernet(llave)
    return f.encrypt(mensaje)

def desencriptar(token: bytes, llave):
    f = Fernet(llave)
    return f.decrypt(token)


def main():
    print("Módulo de criptografía")

    mensaje = "Este es el mensaje super secreto"
    llave: bytes = Fernet.generate_key()
    token = encriptar(bytes(mensaje, 'utf-8'), llave)
    desencriptado = desencriptar(token, llave)
    print(desencriptado)




    

    
if __name__ == "__main__":
    main()
