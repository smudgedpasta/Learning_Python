'''
LEGB
Local, Enclosing, Global, Built-In
'''

a = "global a string"
# ^ Global variables are in the body of the code

def test_zero():
    b = "local b string"
    print(b)
test_zero()   
# ^ Local variables are defined within the function

def test_one():
    b = "local b string"
    print(b)
test_one()

# print(b) < This errors because b cannot be found as a local, enclosing, global or built-in variable
print(a) # < This prints just fine because the code cannot find this variable as local or enclosing, but it is global and defined above

def test_two():
    global a
    a = "Overwriting the global a variable."
    print(a)
test_two()
print(a)

def test_three(c):
    d = "Testing..."
    print(d) # < Change d to c and the output will be the local c variable, thus "Test"
test_three("Test")

e = min([1, 2, 3, 4, 5])
print(e)
# ^ min works because it is a built-in function. The output is 1 because 1 is the smallest

import builtins
print(dir(builtins))

'''
def min():
    pass

f = min([1, 2, 3, 4, 5])
print(f)
^ This errors because defining min in the function will make the code recognise it as a local variable before the built-in function
'''

def outer_function():
    g = "outer function's g"

    def inner_function():
        g = "inner_function's x"
        print(g)
    inner_function()
    print(g)

outer_function()

def outer_function1():
    h = "outer function's h"

    def inner_function1():
        nonlocal h # < This now overwrites the enclosing function, outer_function1()
        h = "inner_function's h"
        print(h)
    inner_function1()
    print(h)

outer_function1()