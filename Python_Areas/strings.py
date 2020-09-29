name = "Smudge" # < String literal
description = '''This is your local Cromch Invading toaster, who can recite 180 Sonic characters
from the top of their memory but practically can't remember anything about maths. :D''' # < Multiline string
print(name)
print(description)
print(name[0])
print(name[0:6])

print(name[ : ]) 
print(name[0 : 7])

fresh = "smudgedpasta"
print("String methods:")
print(len(fresh))
print("The length of this string is", len(fresh))

rotton = " SmUdGeDpAsTa "
print(rotton.strip())
print(rotton.lower().strip())
print(rotton.upper().strip())

name = "Smudge"
print(name.replace("S", "L"))

nums = "1,2,3,4,5,6,7,8,9"
print(nums.split(","))

print('''*
**
***
****
*****''')

print( "Just wanna see if there’s a difference in the space if", "it’s done this way...")
print("... Or this" + "way.")