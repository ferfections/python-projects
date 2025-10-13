from dataclasses import dataclass

@dataclass
class User:
    username: str
    mail: str
    age: int
    
def main():
    user1 = User("fernando", "fng8@alu.ua.es", 24)
    print(user1)

if __name__ == "__main__":
    main()
