for i in range(1,13):
    print("No. {:2} squared is {:3} and cubed is {:4} ".format(i,i**2,i**3))
    print("*" * 80)
#shit+tabbel visszavehető a tabulátor!!


name = input("Please enter your name: ")
age = int(input("How old are you, %s?: "%name))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years {1}".format(18-age,name))

if age < 18:
    print("Please come back in {0} years {1}".format(18-age,name))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")

