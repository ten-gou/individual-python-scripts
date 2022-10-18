list1 = ["hello", "python", 5, 8, ["The", "brown", "fox", "is", "hiding"]]
list2 = ["behind", "the", "fence"]

listStr = list1[4] + list2
#list1[4] is ["The", "Brown"...]
#list2[2] is "fence"
#while the above works for similar types ie. list with list str with str, you cannot mix the two

list2.append(list1[4][2])
#add the str manually through the append method

print(f"listStr is {listStr}")
print(f"list2 is {list2}")