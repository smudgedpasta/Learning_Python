# Lambda functions are "anonymous functions"

def printa(string, a):
    for a in range (a):
        print(string)
printa("Hello", 5)

def multiply(b, c):
    mul = b * c
    return(mul)
d = multiply(4, 8)
print(d)

multiply1 = lambda e, f: e*f
g = multiply1(48, 84)
print(g)

equation = lambda h, i: h/i+20
j = equation(84, 48)
print(j)

MultiInput = lambda k, l, m , n, o, p: k*l*m*n*o*p
q = MultiInput(10, 20, 30, 40, 50, 60)
print(q)