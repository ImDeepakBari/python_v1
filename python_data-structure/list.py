"""
List: Its can contain diff data types ,
all inserted elements holds its position .
Follow FIFO technique.
When appended any elem, added to last index of list.
Can be modified once inserted item to list ,i.e:  mutable
"""

list_1 = [1, 3, True, "Deepak", "", "Where is my life picking up", 34.5, False]


# adding item to list
l1 = [1, 2]
l1.append(3)
print(l1)

l2 = []
l2.insert(0, 9)
l2.insert(1, 10)
l2.insert(3, 88) # here if any inbetween  index is missing then it will insert to that preceding index
print(l2)
print(l2[2])


# slicing
l3 = [2,5, 7,9,30, 56,89, 90]

sliced_list = l3[5]
sliced_list = l3[:] # __eql__ l3[:-1]
sliced_list = l3[::-1] # reversing the entire list
sliced_list = l3[::2] # iterate by step 2

print(sliced_list)


# membership operator
l4 =['Deepak', 'aeiou', "bari", 'superman', False]
print("Deepak" in l4) #true
print("Deepak2" in l4) #False
print(True in l4) #False
print(not True in l4) #True

print("i" in l4) # False

# Removing elements from list
l4 = [4, 78, 566, 4, "ImDeepak", "Hii"]
deleted_item = l4.pop()  # by default remove last index item
print(deleted_item)

deleted_item = l4.pop(4) # removing elements by index value
print(deleted_item)

print(l4)

l10 = ['deepak is to be deleted', 'this is going to be deleted']
print(l10)
del l10[0]
# print(l10)

del l10
# print(l10)


# adding list
l6 = ['one', 'two', 'three', 'four']
l7= [5, 6,7, 8, 9, 10]

added_list = l6 + l7
print(added_list)


# mutable
l8 = [2, 5, 7,0]
l8[0] = 99 # index 0 item 2 is being replaced by value 99
print(l8)


# sorting list items
l11 = [1, 5, 8, 8, 34, 67, 99, 4, 33]
l11.sort()
l11.sort(reverse=True)
print(l11)