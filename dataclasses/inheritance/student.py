from person import Person

class Student(Person):
    def __init__(self, name, age, studies):
        super().__init__(name, age)
        self.studies = studies
    
    def __str__(self):
        return super().__str__() + f"studies={self.studies}"