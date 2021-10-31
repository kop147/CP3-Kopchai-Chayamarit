words = {"Birds": "This is a Birds", "Lab": "Breeds of dog", "Ipad": "Tablet made by Apple",
         "Python": "type of program", "yui": "kop like her"} # key:value
print(words.keys())
for i in words.keys(): #.keys pulls all the keys data
    print(i, end=" ")
print(end="\n")
for i in words.values(): #.value pulls all the values data
    print(i)
