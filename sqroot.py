
# list comp with functions
def square(x):
    return x**2

square_number = [square(x) for x in range(10)]
print(square_number)