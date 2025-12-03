# category numbers are even or odd
categories = []

for num in range(10):
    if num % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")

print(categories)

even_odd = ["Even" if num % 2 == 0 else "Odd" for num in range(10) ]
print(even_odd)