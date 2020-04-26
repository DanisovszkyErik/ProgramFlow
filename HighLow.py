low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

number_of_guesses = 1
guess = None


while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower?"
                     " Enter h or l, or c if my guess was correct: "
                     .format(guess)).casefold()
    if high_low == "h":
        #Guess higher the low end of the range becames 1 greater than the guess
        low = guess + 1

    elif high_low == "l":
        #Guess lower the high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(number_of_guesses))
        break
    else:
        print("Please enter h, l or c")
    # number_of_guesses = number_of_guesses + 1
    number_of_guesses += 1
else:
    print("You thought of the number {0}".format(low))
    print("I got it in {} guesses".format(number_of_guesses))
