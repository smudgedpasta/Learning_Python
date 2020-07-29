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
