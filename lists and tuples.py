'''
There are primarily 4 types if collections in Python. They are:
- list
- tuple
- dictionary
- set
'''

Planets_In_Our_Solar_System = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Planet Nine"]
print(Planets_In_Our_Solar_System)
print(type(Planets_In_Our_Solar_System))
print(Planets_In_Our_Solar_System[0:4])

Example = ["Integer", 100]
print(Example)
print(Example[0])

Planets_In_Our_Solar_System[0] = "Mobius"
print(Planets_In_Our_Solar_System)

print(len(Planets_In_Our_Solar_System))

Planets_In_Our_Solar_System.append("Moebius")
print(Planets_In_Our_Solar_System)

Planets_In_Our_Solar_System.insert(1, "Moebius")
print(Planets_In_Our_Solar_System)

Planets_In_Our_Solar_System.remove("Earth")
print(Planets_In_Our_Solar_System)

Planets_In_Our_Solar_System.pop() # < Can pop a value too
print(Planets_In_Our_Solar_System)

del(Planets_In_Our_Solar_System)

Zodiac_Constellations = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpius", "Sagittarius", "Capricornus", "Aquarius", "Pisces"]

Zodiac_Constellations.remove("Cancer")
print(Zodiac_Constellations)

print(Zodiac_Constellations.index("Gemini"))

Zodiac_Constellations.append("Gemini")
print(Zodiac_Constellations.count("Gemini"))

Zodiac_Constellations.reverse()
print(Zodiac_Constellations)

Zodiac_Constellations.reverse()

Zodiac_Constellations.sort()
print(Zodiac_Constellations)

a = Zodiac_Constellations
b = Zodiac_Constellations.copy()
Zodiac_Constellations.insert(5, "Placeholder")
print(a)
print(b)
a.clear()
print(a)
print(b)

Zodiac_Constellations = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpius", "Sagittarius", "Capricornus", "Aquarius", "Pisces"]
print(max(Zodiac_Constellations))
print(min(Zodiac_Constellations))

Do_you_like = ["My car", "My tractor", "My playmobile"]
Do_you_like[2] = "My attack submarine"
print(Do_you_like)

Do_you_like = ("My car", "My tractor", "My playmobile")
print(type(Do_you_like))
print(Do_you_like[1])
print(len(Do_you_like))
del Do_you_like

Do_you_like = ("My car", "My tractor", "My playmobile")
Do_you_like_2 = list(Do_you_like)
print(Do_you_like_2)
Do_you_like_2[0] = "My flying cactus"
Do_you_like = tuple(Do_you_like_2)
print(Do_you_like)