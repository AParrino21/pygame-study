class Dog():
    """a class to represent a general dog"""
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def eat(self):
        if self.gender == "Male":
            print(f"Here {self.name}! Good boy eat up!")
        else:
            print(f"Here {self.name}! Good girl eat up!")

    def bark(self, is_loud):
        if is_loud:
            print('BARK BARK')
        else:
            print('woof')

dog1 = Dog('Goobis', 'Male', 3)
dog1.eat()
dog1.bark(True)