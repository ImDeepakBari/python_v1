"""
Even number
"""
even = []
for num in range(30):
    if num % 2 == 0:
        even.append(num)

print(even)

even_number = [num for num in range(30) if num %2 == 0]
print(even_number)