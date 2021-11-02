class Animal:
    def eat(self):
        print("Eating Eating!")


class Cat(Animal):
    def eat(self):
        print("Meoww !!")


cat1 = Cat()
cat1.eat()
animal1 = Animal()
animal1.eat()
