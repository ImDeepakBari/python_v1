"""
Sets:
Unordered collection of items
only contains distinct items (no duplicate)
No order is preserved
Represented by set() ie empty set
eg: set_item = {1, 4, 6}
"""

my_set = set()
print(type(my_set)) # class set

# adding item to set
my_set.add(0)
print(my_set)

# adding duplicate item
my_set.add(2)
my_set.add(2)

my_set.add(4)
my_set.add(6)
print(my_set)

# removing item
my_set.remove(4) # this is remove the item
print(my_set)