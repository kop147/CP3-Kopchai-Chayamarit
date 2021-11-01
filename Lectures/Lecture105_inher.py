class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""

    def turn_on_air_conditioner(self):
        print("Turn On : Air")


class Car(Vehicle):
    def say_hello(self):
        print("Hello World!!")


class PickUp(Vehicle):
    load = 20
    def weight_load(self):
        print("This truck can load up to", self.load, "tonnages")


class Van(Vehicle):
    passenger = 15
    def passenger_load(self):
        print("This van can load up to", self.passenger, "people")

class EstateCar(Vehicle):
    passenger = 30

    def passenger_load(self):
        print("This van can load up to", self.passenger, "people")


car1 = Car()
pickup1 = PickUp()
van1 = Van()
estate1 = EstateCar()
car1.turn_on_air_conditioner()
car1.say_hello()
pickup1.turn_on_air_conditioner()
pickup1.weight_load()
van1.turn_on_air_conditioner()
van1.passenger_load()
estate1.turn_on_air_conditioner()
estate1.passenger_load()
