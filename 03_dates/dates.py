import datetime

class User:
    def __init__(self, username):
        self.username = username
        self.creationDate = datetime.datetime.now()

def main():
    user = User("Fernando")
    print(f"username: {user.username}, creationDate: {user.creationDate}")


if __name__ == "__main__":
    main()