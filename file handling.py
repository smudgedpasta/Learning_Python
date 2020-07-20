a = open("TestFile.txt")
content = a.read()
print(content)
a.close()

'''
a = open("TestFile.txt", "r") < This means you want to read the file
a = open("TestFile.txt", "a") < This means you want to append (add more content) to the file
a = open("TestFile.txt", "w") < This means you want to write onto the file, but all former content of the file is erased
a = open("TestFile.txt", "x") < This creates the file (and errors if the file exists already)

By adding a t, for example, a = open("TestFile.txt", "at"), this means you want to handle the file as a text
By adding a b, for example, a = open("TestFile.txt", "ab"), this means you want to handle the file as a binary
'''

a = open("TestFile.txt", "r")
content = a.read()
print(content)
a.close()

a = open("TestFile.txt", "w")
a.write("Test writing text onto the file")
a.close(

a = open("TestFile.txt", "a")
a.write("\nTest appending text onto the file")
a.close()
# ^ This will be concatenated as many times as you run the program

b = open("TestFile2.txt", "x"
c = open("TestFile2.txt", "a")
c.write("Test 🤔")
c.close()