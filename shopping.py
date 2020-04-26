shopping_list = ["milk","pasta","eggs","spam","bread","rice"]


#when we are reach spam in our list, we will skip that value with continue
for item in shopping_list:
    if item == "spam":
        continue
    print("Buy "+ item)