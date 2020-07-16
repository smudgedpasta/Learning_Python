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

x = 4
y = 8
while y>x:
    print(f"The value of x is {x} and the value of y is {y}")
    x = x + 1

index = 0
while index<6:
    print(index)
    index += 1