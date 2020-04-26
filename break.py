shopping_list = ["milk","pasta","eggs","spam","bread","rice"]


#when we are reach spam in our list, we will jump out from a loop
for item in shopping_list:
    if item == "spam":
        break
    print("Buy "+ item)