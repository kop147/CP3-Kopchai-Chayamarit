pLevel = int(input("How many Level?"))
for i in range(pLevel):
    space = (pLevel-i)*" "
    star = ((2*(i+1))-1)*"*"
    print(space, star, space)
