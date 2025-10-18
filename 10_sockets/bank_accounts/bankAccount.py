from dataclasses import dataclass
from users.user import User

@dataclass
class BankAccount:
    id: str
    owner: User
    quantity: int

    def toDict(self):
        return {
            self.id,
            self.owner,
            self.quantity
        }