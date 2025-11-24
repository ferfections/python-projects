import sqlite3
import logging

logger = logging.getLogger('EV_Driver')

logging.basicConfig(
    filename='app.log',  # Nombre del archivo
    level=logging.DEBUG,  # Nivel mínimo a registrar (ej. DEBUG, INFO, WARNING)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class UserManager:
    def __init__(self):
        pass

    def createUserTable(self):
        creationQuery = '''
            CREATE TABLE IF NOT EXISTS Users(
            ID INT PRIMARY KEY NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL)
        '''
        with sqlite3.connect('users.db') as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS users")
            conn.close()

    def deleteUserTable(self):
        pass

def log(msg: str, level="INFO"):
    if level == "INFO":
        logger.info(msg)
    elif level == "WARNING":
        logger.warning(msg)
    elif level == "DEBUG":
        logger.debug(msg)

# --- Punto de Entrada Principal ---
def main():
    logger.info("Iniciando la aplicación web...")
    logger.info('Esto es un log de información')
    logger.warning(f'Esto es ya un warning, y este es el valor')

    

if __name__ == "__main__":
    main()

