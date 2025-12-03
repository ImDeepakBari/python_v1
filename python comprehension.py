"""
This is list all the diff type fo comprehension available in python
"""

# Looping to a range of numbers
value = []
for i in range(100):
    value.append(i)

# print(value)

# using list comprehension
value = [i for i in range(100)]
print(value)

vlaue = [i**2 for i in range(10)]
print(vlaue)