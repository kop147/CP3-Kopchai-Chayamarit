import sys

randomList = [2, 0, 'a']

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print("The reciprocal of", entry, "is", r)
    except:
        print("Oop!", sys.exc_info()[0], "occured.")
        print("Next entry.")
        print()
