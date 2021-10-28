'''Problem1
1
*
2
**
3
***
4
****
5
*****'''
'''Solution1
starNumber = int(input("Please choose a star (1-5)"))
text = ""
for i in range(starNumber):
    text = text+"*"
print(text)'''
''' Solution2
starNumber = int(input("Please choose a star (1-5)"))
print(starNumber*"*") '''

'''problem 2
3
*
**
***
5
*
**
***
****
*****'''
# Solution1
'''stairNum =int(input("How many Stairs?"))
for i in range(stairNum):
    print((i+1)*"*")'''
# Solution2
'''stairnum1 = int(input("How many Stairs?"))
text = ""
for i in range(stairnum1): 
    for y in range(i+1):
        text =((y+1)*"*")
    print(text)    '''
# Solution 3
stairnum1 = int(input("How many Stairs?"))
for i in range(stairnum1):
    text = ""
    for y in range(i+1):
        text += "*"
    print(text)


