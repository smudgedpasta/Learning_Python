'''
Iterable = __iter__()
Iterator = __next__()
Generator = Generators are iterators
'''

# def MemoryDestroyer():
#     list1 = []
#     for a in range(5000000000000000000000000000000000000000000):
#         list1.append(a)
#     return list1
# b = MemoryDestroyer()
# print(b)

def LargeNumber():
    for c in range(5000000000000000000000000000000000000000000):
        yield c 
d = LargeNumber()
print(d.__next__())
print(d.__next__())
print(d.__next__())
print(d.__next__())
print(d.__next__())

name = "John Cena"
iterator = name.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

name2 = "Peppa Pig"
iterator2 = name2.__iter__()
for i in range(len(name2)):
    print(iterator2.__next__())
    i +=1