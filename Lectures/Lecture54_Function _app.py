def login():
    user_input = input("username")
    pass_input = str(input("password"))
    user = "kop"
    password = str(123456)

    if (user_input == user) and (pass_input == password):
        return True
    else:
        return False


def showmenu():
    print("Login successful")
    print("------Kop's Shop--------")
    print("1. Vat calculator")
    print("2. Price Calculator")


def menu_select():
    userSeclected = int(input("Please Choose function (1 or 2)"))
    return userSeclected


def vatCalculate(price):
    vat = 7
    result = int(price) + (int(price) * vat / 100)
    return result


def priceCalculate():
    price1 = int(input("First product Price : "))
    price2 = int(input("Second product Price : "))
    return vatCalculate(price1 + price2)

x=0
while x != True:
    x =login()
showmenu()
if menu_select() ==1:
    price = int(input("How much?"))
    print(vatCalculate(price))
else:
    print(priceCalculate())
