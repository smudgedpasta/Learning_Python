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

num8 = float(input("Enter first number: "))
num9 = float(input("Enter second number: "))
 
def mm(num8=5,num9=6):
	result3=(num8+num9)/2
	return result3
i = mm(num8,num9)
print(i)

def WhatsApp(Status):
    print(f"I don't know what else to have as my {Status}")
    return Status
Status = "status"
a = WhatsApp(Status)

def Greetings(CTE):
    print(f"How are you all doing today, member {CTE}?")
    return()
CTE = input("Enter your name\n")
g = Greetings(CTE)

def Line_Count(num):
    for e in range(1, num + 1):
        print("*" * e)
Lines_Number = int(input("Enter number of lines\n"))
Line_Count(Lines_Number)
