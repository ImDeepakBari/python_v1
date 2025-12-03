# set comprehension
# this only contains unique values

nums = [1,2,4,68,6,9,0,5,4,6,7,8,9,9,6,5,43,2,3,4,6,7]

unique_sets = {i**2 for i in nums}
print(unique_sets)