
inputRound = int(input("Please Enter Rounds :"))
result = 0
for x in range(inputRound):
    y = x
    inputNumber = int(input("x"+str(x+1)+":"))
    result += inputNumber
print(result)

start = int(input("start:"))
step = int(input("step:"))
for i in range(5):
    print(start + step* i,end = "")