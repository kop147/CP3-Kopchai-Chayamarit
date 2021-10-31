tupleExample= ("kop","jack","p","ter")
print(tupleExample)
tupleExample2 = ("dilock", "deaw")
print(tupleExample)
print(tupleExample2)
tupleExample3 = tupleExample + tupleExample2 # can plus and multiple
print(tupleExample3)
print(tupleExample3[3])
print(tupleExample3[:2])
print("kop" in tupleExample3)
for i in tupleExample3:
    print(i, end = " ")