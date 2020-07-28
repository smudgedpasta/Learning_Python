'''
Loops are used to execute a set of statements when the condition is true.
There are primarily 2 types of loops in Python. They are:
- for loops
- while loops
'''

for i in range(10):
    print(i)
    
for i in range(5, 10):
    print(1)

for i in range(2, 10, 2):
    print(i)

for i in range(10, 2, -2):
    print(i)

'''
^ range uses three inputs. Pretending these three values are a, b and c, it starts at a, every loop adds c, then stops at b.
Only one argument would treat b and c as 1 by default.
'''

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

x = 4
y = 8
while y>x:
    print(f"The value of x is {x} and the value of y is {y}")
    x = x + 1

index = 0
while index<6:
    print(index)
    index += 1
    
NumberOfLines_Input = int(input("Please enter the number of lines you wish to count to:\n"))
for a in range(NumberOfLines_Input):
    print(a+1)

for b in range(1, int(input("Enter a number\n",))+1):print(b*"*")

c = int(input("What size shall your pyramid be?\n"))
for d in range(c):
    print(" " * (c-d-1) + " *" * (d+1))

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 4:
        print("Halt!")
        break # < If the break is commented, the Halt! would just print after the 3 and then continue the for loop
    print(num) # < If this print statement was above the conditional, it would've printed out 3

nums1 = [1, 2, 3, 4, 5]
for num1 in nums1:
    if num1 == 4:
        print("Halt!")
        continue 
    print(num1)

nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num2 in nums2:
    for alpha in "abcdefghijklmnopqrstuvwxyz":
        print(num2, alpha)

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

# x = 0
# while True:
#     print(x)
#     x += 1
