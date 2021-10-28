#Example 1
'''if True:
    print("Hello Welcome!")
    if True:
        print("Yo ! Mister A")
        if True:
            print("Ha Ha")'''
# from Lecture 37
user_input = input("username")
pass_input = str(input("password"))
user = "kop"
password = str(123456)

if (user_input == user) and (pass_input == password):
    print("Login successful")
    print("------Kop's Shop--------")
    print("1. Vat calculator")
    print("2. Price Calculator")
    userSeclected = int(input("Please Choose function (1 or 2)"))
    if userSeclected == 1:
        price = int(input("How much is your product"))
        vat = 7
        result = int(price) + (int(price) * vat / 100)
        print(result)
    elif userSeclected ==2:
        price1 = int(input("First product Price : "))
        price2 = int(input("Second product Price : "))
        print(price1+price2)
else:
    print("Please Login again!!!!")

