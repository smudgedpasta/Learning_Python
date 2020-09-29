'''
This is "Object Oreiented Programming"
In object oriented programming, you can model anything in your database to real world scenarios. With:
- Class
- Attributes
- Methods
'''

class Sonic:
    Rings = 10
    Name = "Sonic"
    def RingCount(self):
        return self.Rings
R1 = Sonic() # < Creating a class object called R1
R1.Rings = 342 # < If I comment this, the output is the default Ring Count (10)
print(R1.RingCount()) # < Can also run print(R1.Rings())

'''
Notes regarding classes:
- __init__ is a function that gets called when the class does, which creates the self object and uses it as the first argument
- self is a copy of the class created when the main class is called
- Calling the class twice allows for the __call__ function
'''

class example:
  def __call__(self):
    return "example"
print(example)
print(example()) # < Creates an instance (copy), is what runs __call__ when run in a function
print(example()()) # < example()() is running example().__call__()

# example().__call__() == example.__call__(example())
