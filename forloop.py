parrot = "Norwegian Blue"


for character in parrot:
    print(character)

print()

number = "9,223;372:036 853,775,807"
separatorts = ""

for char in number:
    if not char.isnumeric():
        separatorts = separatorts + char

print(separatorts)

values = "".join(char if char not in separatorts else " " for char in number).split()
print([int(val) for val in values])


