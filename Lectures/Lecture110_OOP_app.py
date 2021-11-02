class Person:
    skinColour = ""
    hair = ""
    gender = ""
    age = ""

    def say_hello(self):
        print("Hello")

    def move(self):
        pass


class Teacher(Person):
    def teach(self):
        pass


class Chef(Person):
    def cook(self):
        pass


class Doctor(Person):
    def treat(self):
        pass


alice = Person()
alice.skinColour = "white"
alice.hair = "short"
alice.gender = "Female"
alice.age = 28
alice.say_hello()
