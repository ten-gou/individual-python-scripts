#search for words with a length above a certain number(8) in a string
inp = int(input("Specify what size of words longer than your input you want found from the string: "))

word_list = "The most beautiful rose is one hardly more than a bud wherein the pangs and ecstasies of desire are working for a larger and finer growth"

arr = word_list.split()

arr2 = []

for x in arr:
    if len(x) >= inp:
        arr2.append(x)

print(arr2)