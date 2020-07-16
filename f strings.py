str1 = "My brain has approximately"
int1 = 100000
str2 = "brain cells, which is 1% the average :D"
brain = "{} {} {}".format(str1, int1, str2)
print(brain)

str1 = "My brain has approximately"
int1 = 100000
str2 = "brain cells, which is 1% the average :D"
print(str1 + " " + str(int1) + " " + str2)

str1 = "My brain has approximately"
int1 = 100000
str2 = "brain cells, which is 1% the average :D"
brain = "{2} {0} {1}".format(str1, int1, str2)
print(brain)

str1 = "According to all known laws of aviation,"
str2 = "there is no way a bee should be able to fly."
str3 = "Its wings are too small to get"
str4 = "its fat little body off the ground."
str5 = "The bee, of course, flies anyway"
str6 = "because bees don't care"
str7 = "what humans think is impossible."
Real_Bee_Movie = "{5} {6} {0} {2} {1} {3} {4}".format(str1, str2, str3, str4, str5, str6, str7)
print(Real_Bee_Movie)

str1 = "My brain has approximately"
int1 = 100000
str2 = "brain cells, which is 1% the average :D"
fstring = f"{str1}" + " " + f"{int1}" + " " + f"{str2}"
print(fstring)

name = "Smudge was born "
dob = "250,000,000"
Legit_Age = f"{name}{dob}"
print(Legit_Age, "terrestrial years ago.")

fresh = "Test"
print(len(fresh))

print(len("Test") == 4)