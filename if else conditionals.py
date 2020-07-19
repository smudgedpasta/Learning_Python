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
    
# Short hand if else notation (ternary operators) is writing the code in condensed, single lines.

a, b = 10**35, 1.67262 # < 10e35 also makes 35 an exponent
c = a-b if a>b else b-a
print(f"The difference between a proton's pressure and a proton's weight is {c}")

print ("The pressure of a proton should never be the same as its weight" if a == b else "A proton's pressure is greater than a proton's weight"
if a > b else "A proton's weight is greater than a proton's pressure")

age = int(input("Enter your age:\n"))
outcome = "You cannot start your driving lessons yet." if age <= 16 else "You boomer, what are you doing here?" if age == 50 else "Dude seriously, you shouldn't be driving at this age." if age == 100 else "You can start your driving lessons."
print("{}".format(outcome))
