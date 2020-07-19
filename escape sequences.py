# Main escape sequences:
# \t = tab
# \n = new line (linefeed)
# \' = single quote
# \" = double quote
# \\ = prints backslash
# \a = bell alert sound
# \b = removes previous character
# \f = formfeed
# \N{name} = prints a unicode character

# print('My name's Smudge') < This will error because of the ' in "name's"

print("My name's Smudge") # < This works because the " and ' are different

print('My name\'s Smudge')

print("\\My name's Smudge\\") # < Two backslashes are interpreted as one

print("My name's Smudge.\t Tabs are a thing I guess. :P")

print("Test\a") # ¯\_(ツ)_/¯

print("ab" + "\b" + "c")

print("My name\fis Smudge")

print(u'\N{DAGGER}')