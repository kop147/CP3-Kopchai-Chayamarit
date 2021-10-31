menuList = []
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Please Enter Price:")
        menuList.append([menuName, menuPrice])


def showBill():
    print("kop restaurant".center(30, "-"))
    print("Items".ljust(15, "-"), "price".rjust(15, "-"))
    for i in range(len(menuList)):
        print(menuList[i][0].ljust(15, "-"), menuList[i][1].rjust(15, "-"))


def total(x):
    total = 0
    for i in range(len(x)):
        total += int(x[i][1])
    return total


showBill()
totalPrice = total(menuList)
print("total price".ljust(15, "-"), str(totalPrice).rjust(15, "-"))
