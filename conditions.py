age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
# if 16 <= age <= 65:
if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enyoj yout free time")
else:
    print("Have a good day at work")

for i in range(101):
    if i % 7 == 0:
        print(i)

for i in range(0,101,7):
    if i % 7 == 0:
        print(i)