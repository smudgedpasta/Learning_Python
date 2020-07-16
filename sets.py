MySet = {1,2,3,4,5,1,2,5,4,3}
a = type(MySet)
print(a)

MySet.add(6)
MySet.update([7, 8, 9, 10])
MySet.remove(1)

b = len(MySet)
print(b)

MySet.discard(11)

c = MySet
print(c)

MySet.clear()
d = MySet
print(d)

del(MySet)

'''
Set methods:
- add()
- clear()
- difference()
- difference_update()
- isdisjoint()
- symmetric_difference()
- union()
- intersection()
'''

a = {3,6,9,12,15,18,21,24,27,30}
b = {4,8,12,16,20,24,28,32,36,40}
print(a.difference(b))
print(a-b)

c = {1,2,3,4,5,6,7,8,9,10,11,12}
d = {1,4,9,16,25,36,49,64,81,100,121,144}
result = c.difference_update(d)
print(c)
print(d)
print(result)
c = c.difference_update(d)
print(c)

e = {2,3,5,7,11,13,17}
f = {19,23,29,31,37,41,43,47}
g = {}
print(e.symmetric_difference(f))
print(f.symmetric_difference(g))

h = {1,4,1,5,9,2,6,5,3,5}
i = {8,9,7,9,3,2,3,8,4,6}
print(h.isdisjoint(i))

j = {"dog", "cat", "fish"}
k = {"cat", "hamster", "gerbil"}
l = {"gerbil", "dog", "guinea pig"}
Pets = j.union(k, l)
print(Pets)

m = {1,2,3,4,5,6,7,8,9,10}
n = {"a","b","c","d","e","f","g","h","i","j"}
Test = m.intersection(n)
print(Test)
o = {1,2,3,4,5,6,7,8,9,10,11,12}
p = {1,4,9,16,25,36,49,64,81,100,121,144}
test = o.intersection(p)
print(test)