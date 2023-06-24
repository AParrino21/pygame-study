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


class Golden(Dog):
    """this class Golden it an extension of the Dog class"""
    def __init__(self, name, age, gender, loves_cheese):
        #call the init from Dog class to all the attributes
        super().__init__()

        self.loves_cheese = loves_cheese
