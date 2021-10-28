userInput = "default"
passInput = "default"
user = "kop"
password = "123456"
while userInput != user or passInput != password:
    userInput = input("Username :")
    passInput = input("Password :")
    if userInput != user or passInput != password:
        print("Fail! Please try again!")
print("Login success!")
