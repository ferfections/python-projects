import json

class User:
    def __init__(self, username, mail, age):
        self.username = username
        self.mail = mail
        self.age = age

    def to_dict(self):
        return {
            "username": self.username,
            "mail": self.mail,
            "age": self.age
        }

    def __str__(self):
        return f"User(username='{self.username}', mail='{self.mail}', age={self.age})"