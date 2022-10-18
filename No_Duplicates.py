listArr = [9,8,7,6,5,4,3,2,1,9,8,7,6,5,4,3,2,1]
duplicate = int(input("Enter the number you want to no duplicates of: "))
num = 0
dup = False

for x in listArr:
    if x == duplicate and dup == True:
        listArr.pop(num)
    elif x == duplicate and dup == False:
        dup = True
    num += 1

print(listArr)