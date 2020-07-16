# Dictionaries are the collection of key-value pairs

dict1 = {
    "Name": "Smudge",
    "Profession": "Comic Artist",
    "Favorite Food": "Pasta",
    "L": [1,2,3,4,5]
}
print(dict1)
print(type(dict1))
print(dict1["Name"])
print(dict1["L"])
print(dict1.get("Favorite Food"))

a = dict1.keys()
print(a)
b = dict1.values()
print(b)
c = dict1.items()
print(c)
d = len(dict1)
print(d)

dict1.pop("L")
print(dict1)

dict1["Favorite Number"] = 4
print(dict1)
del dict1["Favorite Number"]
print(dict1)

dict1.clear()
print(dict1)

Sonic_Characters = {
    "Hedgehog": "Sonic",
    "Fox": "Tails",
    "Echidna": "Knuckles",
    "Human": "Dr Robotnik"
}
print(Sonic_Characters.fromkeys("Hedgehog"))