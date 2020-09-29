a = open("FileHandling_Txts/TestFile.txt")
content = a.read()
print(content)
a.close()

'''
The following examples do not include opening from a folder
If you want to open from a folder, for example, "FileHandling_Txts", it would be: open("FileHandling_Txts/TestFile.txt")

a = open("TestFile.txt", "r") < This means you want to read the file
a = open("TestFile.txt", "a") < This means you want to append (add more content) to the file
a = open("TestFile.txt", "w") < This means you want to write onto the file, but all former content of the file is erased
a = open("TestFile.txt", "x") < This creates the file (and errors if the file exists already)

By adding a t, for example, a = open("TestFile.txt", "at"), this means you want to handle the file as a text
By adding a b, for example, a = open("TestFile.txt", "ab"), this means you want to handle the file as a binary
'''

a = open("FileHandling_Txts/TestFile.txt", "r")
content = a.read()
print(content)
a.close()

# a = open("FileHandling_Txts/TestFile.txt", "w")
# a.write("Test writing text onto the file")
# a.close()

# a = open("FileHandling_Txts/TestFile.txt", "a")
# a.write("\nTest appending text onto the file")
# a.close()
# # ^ This will be concatenated as many times as you run the program

# b = open("FileHandling_Txts/TestFile2.txt", "x"
# c = open("FileHandling_Txts/TestFile2.txt", "a")
# c.write("Test 🤔")
# c.close()

d = open("TestFile.txt")

content = d.read(5)
print(content)
content = d.read(5)
print(content)

line = d.readline()
print(line)

lines = d.readlines()
print(type(lines))

d.close()

e = open("FileHandling_Txts/TestFile.txt")
line2 = e.readline()
print(line2)
e.close()

f = open("FileHandling_Txts/TestFile.txt")
lines2 = f.readlines()
print(lines2)
f.close()
