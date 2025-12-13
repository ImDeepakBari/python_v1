"""
Some useful python function.
"""

# range function
for i in range(1, 10):
    print(i)


# enumerate function
# this function retrurn the tuple object of each item with index position
words = "Where is my country located in world map"
index_value = 0
for ch in words:
    print(f"Character {ch} is located in {index_value}")
    index_value += 1


for index, value in enumerate(words):
    print(f"Character {value} located in index {index}")


# zip function
# this function zip the two iterable object
list1 = [1, 3, 6]
list2 = ['a', 'c', 'd']

for item in zip(list1, list2):
    print(item)


# unequal list
l1 = [1, 4, 6, 7]
l2 = ['a', 'b']

for item in zip(l1, l2):
    print(item)