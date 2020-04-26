import random



highest = 10

answer = random.randint(1,highest)
print(answer) #TODO: ez nagyon meno ez a Todo komment INTELIJJ TODO füül!!
print("Please guess a number between 1 and {}: ".format(highest))
guess = None


while guess != answer:
    guess = int(input())
    if guess == answer:
        print("You got it")
        break
    elif guess == 0:
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")

if guess == 0:
    print("Man why aren't you played along this funny game. Idiot")





# if guess < answer:
#     print("Please guess higher!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
# if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it bro")
