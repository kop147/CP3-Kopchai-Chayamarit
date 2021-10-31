try:
    input1 = int(input("A:"))
    input2 = int(input("B:"))
    print(input1/input2)
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("zero division error")
except :
    print("error!")
