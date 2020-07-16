age = int(input("Enter your age:\n"))
print(f"Your age is {age}")
if age>=17:
    print("You can start your driving lessons.")
else:
    print("You cannot start your driving lessons yet.")

age = int(input("Enter your age:\n"))
print(f"Your age is {age}")
if  age<=16:
    print("You cannot start your driving lessons yet.")
elif age==50:
    print("You boomer, what are you doing here?")
elif age==100:
    print("Dude seriously, you shouldn't be driving at this age.")
else:
    print("You can start your driving lessons.")

age = int(input("Enter your age:\n"))
print(f"Your age is {age}")
name = input("Enter your name:\n")
if  age<=16 or name != "Smudge":
    print("You cannot start your driving lessons yet.")
elif age==50:
    print("You boomer, what are you doing here?")
elif age==100:
    print("Dude seriously, you shouldn't be driving at this age.")
else:
    print("You can start your driving lessons.")

num = int(input("Please enter a number:\n"))
if num > 100:
    print("You have entered a huge, three or more digit number!")
else:
    print("You have entered a small, 1 or two digit number!")