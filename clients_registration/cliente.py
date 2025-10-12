import json

class Cliente:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def getUsername(self):
        return self.username
    
    def getUserEmail(self):
        return self.email
    
    def getUserPassword(self):
        return self.password
    
    def storeInJson(self, filename):
        pass