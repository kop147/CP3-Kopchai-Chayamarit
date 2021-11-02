class Animal:
    def eat(self):
        print("Eating Eating!")


class Cat(Animal):

    def set_name(self,text):  # Setter = function for set value , Getter = function for get value
        __name = ""
        self.name = text
        print("Setting New cat name = ", self.name)

    def eat(self):
        print("Meoww !!", self.name)


cat1 = Cat()
cat1.set_name("TT")
cat1.eat()
print(cat1.name)
