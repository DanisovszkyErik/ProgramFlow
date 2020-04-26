shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

item_to_find = "spam"
found_at = None
#So the len() function is return with the sequence length
# for i in range(6) now range(6) eqivalent with len(shopping_list) cuz the list lenght is 6
# for i in range(len(shopping_list)):
#     if shopping_list[i] == item_to_find:
#         found_at = i
#         break


if  item_to_find in shopping_list:
    #list.index("asdas") megadja hogy "asdas" elem hol helyezkedik el a listánkban
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position: {}".format(found_at))
else:
    print("{} not found".format(item_to_find))