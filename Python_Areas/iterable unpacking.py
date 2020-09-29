print(list(enumerate(["abc", "def", "ghi", "jkl"])))
# ^ enumrate lists the contents from a list with a paired number

a, b, c = (1, 2, 3)
print(a, b, c)

for i, c in enumerate(["abc", "def", "ghi", "jkl"]):
  print(i, c)

print(["abc", "def", "ghi", "jkl"].index("def"))
# ^ index prints the position

print(["abc", "def", "ghi", "jkl"][1])
# ^ This prints the elements of a position