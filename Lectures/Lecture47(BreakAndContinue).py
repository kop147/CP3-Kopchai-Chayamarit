for y in range(1,13):
    break
    for x in range(12):
        print(y, "x", x+1, "=", y*(x+1))
    break   # the order for break the loop

for val in "hello":
    if val =="l":
        continue  # skip the round only not the loop
    print(val)

print("The End")
