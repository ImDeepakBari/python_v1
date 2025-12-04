"""
tuple: Its are immutable
once item are added its cannot be modified or alter
tuple uses () parenthesis for defining
tuple holds order of items inserted
store diff datatypes as list
"""
from itertools import count
from operator import countOf

t1 = (1, 3, 56,8)
print(type(t1)) # tuple class

print(len(t1)) # 4

#slicing
print(t1[2]) # 56

# modification/altering/updating
# diff = t1[0] = 8  #TypeError: 'tuple' object does not support item assignment
# print(diff)

# counter function
t2 = ('a', 'a', 'b')
print(t2.count('a')) # 2 count
print(t2.count('b')) # 1 count

# index function
t4 = ('k', 'k', 'l', 'o', 'l')
print(t4.index('l')) # index 2 i.e return the first occurance


# important tuple assigments
a, b ,c = ("Sunday", "Monday", "tuesday")
print(a, b, c)
t5 = [(3,5,6), (35,54,64), (9,5,3), (32, 5,6)]
for i, j, k in t5:
    print(i)
    print(j)
    print(k)
    print(i, j, k)



# dict
d = {'name': 'deepak', 'org': "GL", 'Isemployed': True}

for key, value in d.items():
    print(value)
    print(key,":" ,value)