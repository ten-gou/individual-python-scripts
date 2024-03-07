lst_01 = ["Bye ", "take ", "blue"]
lst_02 = ["John", "Sir", "building", "truck"]

output = []

for x in lst_01:
    for y in lst_02:
        string = x + y
        output.append(string)

print(output)