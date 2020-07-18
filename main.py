print("According to all known laws of aviation, there should be no way that be is able to fly.")

'''
test
'''

print(" ")

a = 34.87
b = 45
print("This is the value of: ", a, b) 

Test_One = 50
Test_Two = 300
print("The variables of Test_One and Test_Two equal to", Test_One, "and", Test_Two) 

'''
Data types in Python
Numbers, Strings, Booleans, List, Tuples, Sets, Dictionaries
Numbers: Int, Float, Complex
'''

c = "true"
d = 1 + 5j
e = "this"
f = [1,2,3]
print(type(c))
print(type(d))
print(type(e))
print(type(f))

globals().clear()
print(" ")

num1 = 45
num2 = 46

print(num1 + num2)

'''
Rules to creating variables in Python:
- Must start with a letter or an underscore
- A variable cannot start with a number
- Variables are case sensitive
- Can only contain underscores and alpha numeric characters

The three types of Python numbers:
- int
- float
- complex
'''

x = 1 # < This is an integer (int) numeric datatype
y = 1.11 # < This is a float numeric datatype
z = 1 + 5j # < This is a complex numeric datatype

print(x,y,z)

c = int(y)
print(c) 
d = float(x)
print(c,d)

globals().clear()
print(" ")

'''
Operators in Python:
- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
'''

a = 4
b = 56
print("The value of a + b is", a + b)
print("The value of a - b is", a - b)
print("The value of a * b is", a * b)
print("The value of a / b is", a / b)
print("The value of a // b is", a // b)
print("The value of a % b is", a % b)

c = 45
d = 78
d += 3
print(d)
d -= 3
print(d)
d *= 3
print(d)
d /= 3
print(d)
d //= 3
print(d)
d %= 3
print(d)

e = 98
f = 87
g = e>f
print(g)
print(type(g))
h = f>e
print(h)
i = e != f 
print(i)
j = e == f 
print(j)
k = e == 98
print(k)
l = e >= 98
print(l)
m = e <= 98
print(m)

'''
The three primary Logical Operators:
- and
- or
- not
'''

n = True and False
print(n)
o = True or False
print(o)
p = not False
print(p)
q = not True
print(q)

globals().clear()
print(" ")

name = "Smudge" # < String literal
description = '''This is your local Cromch Invading toaster, who can recite 180 Sonic characters
from the top of their memory but practically can't remember anything about maths. :D''' # < Multiline string
print(name)
print(description)
print(name[0])
print(name[0:6])
print(name[ : ]) 
print(name[0 : 7])

fresh = "smudgedpasta"
print("String methods:")
print(len(fresh))
print("The length of this string is", len(fresh))

rotton = " SmUdGeDpAsTa "
print(rotton.strip())
print(rotton.lower().strip())
print(rotton.upper().strip())

name = "Smudge"
print(name.replace("S", "L"))
nums = "1,2,3,4,5,6,7,8,9"
print(nums.split(","))

print('''*
**
***
****
*****''')

globals().clear()
print(" ")

print( "Just wanna see if there’s a difference in the space if", "it’s done this way...")
print("... Or this" + "way.")

str1 = "My brain has approximately"
int1 = 100000
str2 = "brain cells, which is 1% the average :D"
brain = "{} {} {}".format(str1, int1, str2)
print(brain)

str1 = "My brain has approximately"
int1 = 100000
str2 = "brain cells, which is 1% the average :D"
print(str1 + " " + str(int1) + " " + str2)

str1 = "My brain has approximately"
int1 = 100000
str2 = "brain cells, which is 1% the average :D"
brain = "{2} {0} {1}".format(str1, int1, str2)
print(brain)

str1 = "According to all known laws of aviation,"
str2 = "there is no way a bee should be able to fly."
str3 = "Its wings are too small to get"
str4 = "its fat little body off the ground."
str5 = "The bee, of course, flies anyway"
str6 = "because bees don't care"
str7 = "what humans think is impossible."
Real_Bee_Movie = "{5} {6} {0} {2} {1} {3} {4}".format(str1, str2, str3, str4, str5, str6, str7)
print(Real_Bee_Movie)

str1 = "My brain has approximately"
int1 = 100000
str2 = "brain cells, which is 1% the average :D"
fstring = f"{str1}" + " " + f"{int1}" + " " + f"{str2}"
print(fstring)

name = "Smudge was born "
dob = "250,000,000"
Legit_Age = f"{name}{dob}"
print(Legit_Age, "terrestrial years ago.")

fresh = "Test"
print(len(fresh))

print(len("Test") == 4)

globals().clear()
print(" ")

# str1 = "What is your name?"
# name = input(str1)
# print(f"My name is {name}")

# str1 = "What is your name?\n"
# name = input(str1)
# print(f"My name is {name}")

# str1 = "What is your name?\n"
# name = input(str1)
# print(f"My name is {name}", end = " ")
# print("This is just a test.")

# num1 = input("Enter first number\n")
# num2 = input("Enter second number\n")
# print(f"The sum of {num1} and {num2} is {int(num1) + int(num2)}")

# num1 = int(input("Enter first number\n"))
# num2 = int(input("Enter second number\n"))
# print(f"The sum of {num1} and {num2} is {num1 + num2}")

# str1 = "What is your name?\n"
# name1 = input(str1)
# str2 = "Very interesting, now what's your name?\n"
# name2 = input(str2)
# str3 = "Mhm, mhm, very nice, now what's your name?\n"
# name2 = input(str3)
# str4  = "Uhuh that's very nice, now would you like to tell me your name?\n"
# name2 = input(str4)
# str5 = "That's nice, but I don't think I know your name yet. What's your name?\n"
# name2 = input(str5)
# print(f"I think I have concluded that your name might possibly be {name1}")

# globals().clear()
print(" ")

'''
There are primarily 4 types if collections in Python. They are:
- list
- tuple
- dictionary
- set
'''

Planets_In_Our_Solar_System = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Planet Nine"]
print(Planets_In_Our_Solar_System)
print(type(Planets_In_Our_Solar_System))
print(Planets_In_Our_Solar_System[0:4])

Example = ["Integer", 100]
print(Example)
print(Example[0])

Planets_In_Our_Solar_System[0] = "Mobius"
print(Planets_In_Our_Solar_System)

print(len(Planets_In_Our_Solar_System))

Planets_In_Our_Solar_System.append("Moebius")
print(Planets_In_Our_Solar_System)

Planets_In_Our_Solar_System.insert(1, "Moebius")
print(Planets_In_Our_Solar_System)

Planets_In_Our_Solar_System.remove("Earth")
print(Planets_In_Our_Solar_System)

Planets_In_Our_Solar_System.pop() # < Can pop a value too
print(Planets_In_Our_Solar_System)

del(Planets_In_Our_Solar_System)

Zodiac_Constellations = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpius", "Sagittarius", "Capricornus", "Aquarius", "Pisces"]

Zodiac_Constellations.remove("Cancer")
print(Zodiac_Constellations)

print(Zodiac_Constellations.index("Gemini"))

Zodiac_Constellations.append("Gemini")
print(Zodiac_Constellations.count("Gemini"))

Zodiac_Constellations.reverse()
print(Zodiac_Constellations)

Zodiac_Constellations.reverse()

Zodiac_Constellations.sort()
print(Zodiac_Constellations)

a = Zodiac_Constellations
b = Zodiac_Constellations.copy()
Zodiac_Constellations.insert(5, "Placeholder")
print(a)
print(b)
a.clear()
print(a)
print(b)

Zodiac_Constellations = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpius", "Sagittarius", "Capricornus", "Aquarius", "Pisces"]
print(max(Zodiac_Constellations))
print(min(Zodiac_Constellations))

globals().clear()
print(" ")

Do_you_like = ["My car", "My tractor", "My playmobile"]
Do_you_like[2] = "My attack submarine"
print(Do_you_like)

Do_you_like = ("My car", "My tractor", "My playmobile")
print(type(Do_you_like))
print(Do_you_like[1])
print(len(Do_you_like))
del Do_you_like

Do_you_like = ("My car", "My tractor", "My playmobile")
Do_you_like_2 = list(Do_you_like)
print(Do_you_like_2)
Do_you_like_2[0] = "My flying cactus"
Do_you_like = tuple(Do_you_like_2)
print(Do_you_like)

globals().clear()
print(" ")

# Dictionaries are the collection of key-value pairs

dict1 = {
    "Name": "Smudge",
    "Profession": "Comic Artist",
    "Favorite Food": "Pasta",
    "L": [1,2,3,4,5]
}
print(dict1)
print(type(dict1))
print(dict1["Name"])
print(dict1["L"])
print(dict1.get("Favorite Food"))

a = dict1.keys()
print(a)
b = dict1.values()
print(b)
c = dict1.items()
print(c)
d = len(dict1)
print(d)

dict1.pop("L")
print(dict1)

dict1["Favorite Number"] = 4
print(dict1)
del dict1["Favorite Number"]
print(dict1)

dict1.clear()
print(dict1)

Sonic_Characters = {
    "Hedgehog": "Sonic",
    "Fox": "Tails",
    "Echidna": "Knuckles",
    "Human": "Dr Robotnik"
}
print(Sonic_Characters.fromkeys("Hedgehog"))

globals().clear()
print(" ")

MySet = {1,2,3,4,5,1,2,5,4,3}
a = type(MySet)
print(a)

MySet.add(6)
MySet.update([7, 8, 9, 10])
MySet.remove(1)

b = len(MySet)
print(b)

MySet.discard(11)

c = MySet
print(c)

MySet.clear()
d = MySet
print(d)

del(MySet)

'''
Set methods:
- add()
- clear()
- difference()
- difference_update()
- isdisjoint()
- symmetric_difference()
- union()
- intersection()
'''

a = {3,6,9,12,15,18,21,24,27,30}
b = {4,8,12,16,20,24,28,32,36,40}
print(a.difference(b))
print(a-b)

c = {1,2,3,4,5,6,7,8,9,10,11,12}
d = {1,4,9,16,25,36,49,64,81,100,121,144}
result = c.difference_update(d)
print(c)
print(d)
print(result)
c = c.difference_update(d)
print(c)

e = {2,3,5,7,11,13,17}
f = {19,23,29,31,37,41,43,47}
g = {}
print(e.symmetric_difference(f))
print(f.symmetric_difference(g))

h = {1,4,1,5,9,2,6,5,3,5}
i = {8,9,7,9,3,2,3,8,4,6}
print(h.isdisjoint(i))

j = {"dog", "cat", "fish"}
k = {"cat", "hamster", "gerbil"}
l = {"gerbil", "dog", "guinea pig"}
Pets = j.union(k, l)
print(Pets)

m = {1,2,3,4,5,6,7,8,9,10}
n = {"a","b","c","d","e","f","g","h","i","j"}
Test = m.intersection(n)
print(Test)
o = {1,2,3,4,5,6,7,8,9,10,11,12}
p = {1,4,9,16,25,36,49,64,81,100,121,144}
test = o.intersection(p)
print(test)

globals().clear()
print(" ")

# age = int(input("Enter your age:\n"))
# print(f"Your age is {age}")
# if age>=17:
#     print("You can start your driving lessons.")
# else:
#     print("You cannot start your driving lessons yet.")

# age = int(input("Enter your age:\n"))
# print(f"Your age is {age}")
# if  age<=16:
#     print("You cannot start your driving lessons yet.")
# elif age==50:
#     print("You boomer, what are you doing here?")
# elif age==100:
#     print("Dude seriously, you shouldn't be driving at this age.")
# else:
#     print("You can start your driving lessons.")

# age = int(input("Enter your age:\n"))
# print(f"Your age is {age}")
# name = input("Enter your name:\n")
# if  age<=16 or name != "Smudge":
#     print("You cannot start your driving lessons yet.")
# elif age==50:
#     print("You boomer, what are you doing here?")
# elif age==100:
#     print("Dude seriously, you shouldn't be driving at this age.")
# else:
#     print("You can start your driving lessons.")

# num = int(input("Please enter a number:\n"))
# if num > 100:
#     print("You have entered a huge, three or more digit number!")
# else:
#     print("You have entered a small, 1 or two digit number!")

# Short hand if else notation (ternary operators) is writing the code in condensed, single lines

a, b = 10**35, 1.67262 # < 10e35 also makes 35 an exponent
c = a-b if a>b else b-a
print(f"The difference between a proton's pressure and a proton's weight is {c}")

print ("The pressure of a proton should never be the same as its weight" if a == b else "A proton's pressure is greater than a proton's weight"
if a > b else "A proton's weight is greater than a proton's pressure")

globals().clear()
print(" ")

'''
Loops are used to execute a set of statements when the condition is true.
There are primarily 2 types of loops in Python. They are:
- for loops
- while loops
'''

for i in range(10):
    print(i)

myList = ["This", "That", "Smudge", "Perfect", 45]
for a in myList:
    print(a)

myTuple = (1, 2, 3, 4, 5, "Smudge")
for b in myTuple:
    print(b)

myDict = {
    "name": "Smudge",
    "favorite color": "purple",
    "favorite number": 4
}
for c in myDict.items():
    print(c)

myDict = {
    "name": "Smudge",
    "favorite color": "purple",
    "favorite number": 4
}
for key, value in myDict.items():
    print(f"The key is {key} and the value is {value}")

StudentMarks = {
    "Timothy": 7,
    "Jacob": 10,
    "Austin": 4,
    "Sarah": 7,
    "Gabriel": 5,
    "Lewis": 9
}
for key, value in StudentMarks.items():
    print(f"Name of student: {key} Grade out of 10: {value}")

StudentMarks = {
    "Timothy": 7,
    "Jacob": 10,
    "Austin": 4,
    "Sarah": 7,
    "Gabriel": 5,
    "Lewis": 9
}
for key, value in StudentMarks.items():
    print(f"Name of student: {key} Grade out of 10: {value}")

globals().clear()
print(" ")

x = 4
y = 8
while y>x:
    print(f"The value of x is {x} and the value of y is {y}")
    x = x + 1

index = 0
while index<6:
    print(index)
    index += 1
    
# NumberOfLines_Input = int(input("Please enter the number of lines you wish to count to:\n"))
# for a in range(NumberOfLines_Input):
#     print(a+1)

# for b in range(1, int(input("Enter a number\n",))+1):print(b*"*")

# c = int(input("What size shall your pyramid be?\n"))
# for d in range(c):
#     print(" " * (c-d-1) + " *" * (d+1))

globals().clear()
print(" ")

# name = input("Enter your name\n")
# print(f"Your capitalized name is {name.capitalize()}")
# print(f"Your capitalized name is {name[0].upper() + name[1:]}")
# print(int(input("Please enter a number\n")))

# globals().clear()
print(" ")

def greeting(name):
    print(f"Good morning, {name}")
    return 0 # < this makes "greeting" return 0

name = "Sonic"
name1 = "Manic"
name2 = "Sonia"

g = greeting(name)
g2 = greeting(name1)
g3 = greeting(name2)

print(g, g2, g3)
# ^ return makes whatever value following it be the return value. In this case, the return value of "greeting" is 0

def add(num1, num2):
    result = num1 + num2
    return result

a = 50
b = 100
c = add(a, b)
print(c)

def plus(num3, num4=4): # < 4 is num4's default value when it is not parsed below
    result1 = num3 + num4
    return result1

d = 50
e = plus(d)
print(e)

def mean(num5, num6):
    num7 = num5 + num6
    result2 = num7 / 2
    return result2

f = 44
g = 84
h = mean(f, g)
print(h)

# num8 = float(input("Enter first number: "))
# num9 = float(input("Enter second number: "))
 
# def mm(num8=5,num9=6):
# 	result3=(num8+num9)/2
# 	return result3
# i = mm(num8,num9)
# print(i)

def WhatsApp(Status):
    print(f"I don't know what else to have as my {Status}")
    return Status
Status = "status"
a = WhatsApp(Status)

# def Line_Count(num):
#     for e in range(1, num + 1):
#         print("*" * e)
# Lines_Number = int(input("Enter number of lines\n"))
# Line_Count(Lines_Number)

globals().clear()
print(" ")

'''
Examples of factorials:

6! = 6 x 5 x 4 x 3 x 2 x 1
^ This is factorial(6)

6! = 6 x 5!
^ factorial(6) = 6 x factorial(5)

factorial(n) = n x factorial(n-1)
^ This statement is True only for n>=1

4! = 4 x 3 x 2 x 1 = 24
3! = 3 x 2 x 1 = 6
2! = 2 x 1 = 2
1! = 1
0! = 1
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

fac = factorial(4)
print(fac)

fac = factorial(0) # < This has an output of 1 because it is hardcoded for 0 to have a value of 1
print(fac)

'''
4! = 4 x 3!
4! = 4 x 3 x 2!
4! = 4 x 3 x 2 x 1! < 1 is hard coded in the function to have a value of 1
4! = 4 x 3 x 2 x 1 = 24
'''

def factorial1(n):
     if n == 0 or n == 1:
        return 1
     return n * factorial1(n - 1)

fac = factorial1(3)
print(fac)

def testing_factorials(a):
    if a <= 1:
        return 1
    return a * testing_factorials(a - 3) # < The - 3 in this case means it goes down by 3 places each time, as appose to the usual 1

test_fac = testing_factorials(5)
print(test_fac)

globals().clear()
print(" ")

# from __future__ import braces

import math

'''
import math as m
^ this does the same thing on the code below, just condensed down to "m"

example:
a = 3.14159
print(m.floor(a))
'''

a = 3.14159
print(math.floor(a))

b = 3.14159
print(math.ceil(b))

print(math.factorial(6))

import this 
# import antigravity

globals().clear()
print(" ")

CaveStory_Characters = ["Quote", "Curly", "Toroko", "Arthur", "Sue", "Misery", "Balrog"]

for item in CaveStory_Characters:
    print(f"One of the characters from Cave Story is {item}")
    if item == "Arthur": # < If this item does not exist, the break statement won't execute
        break # < This prevents the else statement and everything else on the list from executing
else:
    print("This else comes after the for loop.")

More_CaveStory_Characters = {
    "Kazuma": "Sakamoto",
    "Momorin": "Sakamoto",
    "King": "the Mimiga",
    "Jack": "the Mimiga",
    "Jenka": "the Witch",
    "Ballos": "the Potato Head"
}

for key in More_CaveStory_Characters:
  print(key, "-", More_CaveStory_Characters[key])

globals().clear()
print(" ")

'''
Let's pretend I'm pulling some data from the internet:

block 1 - import statements
block 2 - calculations
block 3 - pulling some data
block 4 - perform data processing
block 5 - return the result
'''

# a_a = 5
# b_b = int(input("Enter b_b\n"))
# c_c = a_a + b_b

# # ServerData will return True only if data pull is a success
# ServerData = False
# try:
#     if (ServerData):
#          d_d = 6
#     print(d_d)

#     print("Success")

# except Exception as e_e:
#     print(f"Data pull failed because of the following error: {e_e}")

# f_f = int(input("Enter f_f\n"))

# Test = False
# try:
#     if (Test):
#         g_g = 5
#     print(g_g)

#     print("Successfully executed.")

# except Exception as h_h:
#     print(f"Test failed because of the following error: {repr(h_h)}")

# a_a = int(input("Enter a_a\n"))

# Test = False
# try:
#     if (Test):
#         b_b = 5
#     print(b_b)

#     print("Successfully executed.")

# except Exception as c_c:
#     print(f"Test failed because of the following error: {repr(c_c)}")
    
# # ^ This code executed because the variables are not assigned to Test

# globals().clear()
print(" ")
