#ex1
'''correct_number = 17
user_guess = 0
while user_guess != correct_number:
    user_guess = int(input("Please guess a number: "))
    if user_guess > correct_number:
        print("Too Large")
    elif user_guess < correct_number:
        print("Too Small")
    elif user_guess == correct_number:
        print("Correct!!!!")'''
#ex2
correct_number = 17
user_guess = 0
while user_guess != correct_number:
    user_guess = int(input("Please guess a number: "))
    if user_guess > correct_number:
        print("Too Large")
    elif user_guess < correct_number:
        print("Too Small")
print("Correct!!!!")