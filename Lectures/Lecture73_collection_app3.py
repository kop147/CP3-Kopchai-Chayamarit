menuPriceList = {"rice": 50, "soup": 30, "egg": 20}
myMenu = []
while True:
    menuInput = input("Enter menu :")
    if menuInput.lower() == "exit":
        break
    else:
        myMenu.append([menuInput.lower(), str(menuPriceList[menuInput])])


def showBill():
    print("kop restaurant".center(30, "-"))
    print("Items".ljust(15, "-"), "price".rjust(15, "-"))
    for i in range(len(myMenu)):
        print(myMenu[i][0].ljust(15, "-"), myMenu[i][1].rjust(15, "-"))


def total(x):
    total = 0
    for i in range(len(x)):
        total += int(x[i][1])
    return total


showBill()
totalPrice = total(myMenu)
print("total price".ljust(15, "-"), str(totalPrice).rjust(15, "-"))




