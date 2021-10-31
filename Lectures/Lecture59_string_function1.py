name = input("Firstname:").capitalize()
lastname = input("Lastname:").capitalize()
print("Hello %s %s" % (name, lastname))

text = "Kop"
textformated = "welcome %s" % name
print("---------Welcome-------")
print(textformated.center(30,"-"))
print(len(name))
