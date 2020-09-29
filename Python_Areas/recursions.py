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