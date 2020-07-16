'''
Let's pretend I'm pulling some data from the internet:

block 1 - import statements
block 2 - calculations
block 3 - pulling some data
block 4 - perform data processing
block 5 - return the result
'''

a_a = 5
b_b = int(input("Enter b_b\n"))
c_c = a_a + b_b

# ServerData will return True only if data pull is a success
ServerData = False
try:
    if (ServerData):
         d_d = 6
    print(d_d)

    print("Success")

except Exception as e_e:
    print(f"Data pull failed because of the following error: {e_e}")

f_f = int(input("Enter f_f\n"))

Test = False
try:
    if (Test):
        g_g = 5
    print(g_g)

    print("Successfully executed.")

except Exception as h_h:
    print(f"Test failed because of the following error: {repr(h_h)}")

a_a = int(input("Enter a_a\n"))

Test = False
try:
    if (Test):
        b_b = 5
    print(b_b)

    print("Successfully executed.")

except Exception as c_c:
    print(f"Test failed because of the following error: {repr(c_c)}")
    
# ^ This code executed because the variables are not assigned to Test