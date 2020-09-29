str1 = "What is your name?"
name = input(str1)
print(f"My name is {name}")

str1 = "What is your name?\n"
name = input(str1)
print(f"My name is {name}")

str1 = "What is your name?\n"
name = input(str1)
print(f"My name is {name}", end = " ")
print("This is just a test.")

num1 = input("Enter first number\n")
num2 = input("Enter second number\n")
print(f"The sum of {num1} and {num2} is {int(num1) + int(num2)}")

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
print(f"The sum of {num1} and {num2} is {num1 + num2}")

str1 = "What is your name?\n"
name1 = input(str1)
str2 = "Very interesting, now what's your name?\n"
name2 = input(str2)
str3 = "Mhm, mhm, very nice, now what's your name?\n"
name2 = input(str3)
str4  = "Uhuh that's very nice, now would you like to tell me your name?\n"
name2 = input(str4)
str5 = "That's nice, but I don't think I know your name yet. What's your name?\n"
name2 = input(str5)
print(f"I think I have concluded that your name might possibly be {name1}")

name = input("Enter your name\n")
print(f"Your capitalized name is {name.capitalize()}")
print(f"Your capitalized name is {name[0].upper() + name[1:]}")
print(int(input("Please enter a number\n")))