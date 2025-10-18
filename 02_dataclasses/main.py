from dataclasses import dataclass

@dataclass
class User:
    """ User class """
    username: str
    mail: str
    age: int


    def toDict(self):
        return {
            self.username,
            self.mail,
            self.age
        }

def main():    
    """ Block comment """
    user1 = User("fernando", "fernando@alu.ua.es", 24)
    print(user1)

if __name__ == "__main__":
    main()
