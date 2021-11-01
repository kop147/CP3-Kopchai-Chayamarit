class Customer:
    name = ""
    lastName = ""
    age = 0

    def add_cart(self):
        print("Added to", self.name, self.lastName, "'s Cart")

customer1 = Customer()
customer1.name = "kopchai"
customer1.lastName = "Chayamarit"
customer1.age = 40
customer1.add_cart()
customer2 = Customer()
customer2.name = "Sitthikorn"
customer2.lastName = "Lorgunpai"
customer2.age = 39
customer2.add_cart()
customer3 = Customer()
customer3.name = "Peerapun"
customer3.lastName = "Chivapornthip"
customer3.age = 40
customer4 = Customer()
customer4.name = "Chaivit"
customer4.lastName = "Aroonnatethong"
customer4.age = 39
customer4.add_cart()
customer1.add_cart()
