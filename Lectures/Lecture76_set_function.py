'''fruits = {"apple", "banana", "pineapple", "orange"}
print(fruits)
# del fruits  delete the whole set
fruits.remove("banana")
print(fruits)
fruits.add("grape")
print(fruits)'''

#example
myFruits = set()
userInput = int(input("Enter number of your favorite fruits :"))
while len(myFruits) < userInput:
    myFruits.add(input("Name your favorite fruits").lower())
print(myFruits)
