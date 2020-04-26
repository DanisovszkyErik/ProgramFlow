options = ["Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed", "Exit"]
choosen_option = len(options)+1

while choosen_option != 0:
    if choosen_option >= len(options):
        print("Please choose your option from the list below:")
        for option in options:
            if option != "Exit":
                print("{0}. {1}".format(options.index(option) +1,option))
            else:
                print("{0}. {1}\n".format(0 ,option))
    else:
        print("You choosed {}. Congrats that was a {} row in our list"
                .format(options[choosen_option-1],choosen_option))

    choosen_option = int(input())



