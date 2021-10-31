menuList = []
pricelist = []
menu = {}
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Please Enter Price:")
        menuList.append(menuName)
        pricelist.append(menuPrice)


def showBill():
    print("kop restaurant".center(30, "-"))
    print("Items".ljust(15, "-"), "price".rjust(15, "-"))
    for i in range(len(menuList)):
        print(menuList[i].ljust(15, "-"), pricelist[i].rjust(15, "-"))

'''solution 1
for i in range(len(menuList)):
    menu[menuList[i]] = pricelist[i] '''


def total(x):
    total = 0
    for i in range(len(x)):
        total += int(x[i])
    return total


showBill()
totalPrice = total(pricelist)

print("totalprice".ljust(15, "-"), str(totalPrice).rjust(15, "-"))




