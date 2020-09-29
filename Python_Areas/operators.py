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

# True and False are Booleans
