options = ['apple', 'mango', 'orange', 'banana', 'pineapple', 'water-melon', '', 'elephant', 'a_teste']
# check the string strats with 'a' and end with 'e'
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue

    if string[0] != 'a':
        continue

    if string[-1] != 'e':
        continue

    valid_strings.append(string)

print(valid_strings)


valid_str = [
    string for string in options if len(string) >= 2
                                    if string[0] == 'a'
                                       if string[-1] == 'e'
]
print(valid_str)