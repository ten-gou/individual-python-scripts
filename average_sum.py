words = '''On the 8 day of Christmas my true love sent to me
48 maids a miling
28 swans a swimming
12 geese a laying
144 gold rings
50 calling birds
10 French hens
21 turtledoves
And 23 partridge in a pear tree'''

def sum_average(input):
    arr = [*words]
    sum = 0
    amt = 0

    for x in arr:
        numberCheck = x.isdigit()
        if numberCheck == True:
            sum += int(x)
            amt += 1

    avg = sum/amt
    rounded = round(avg, 2)

    output = f"Averaging out all the digits of the inputted string, the output rounds out to {rounded}, to two decimal places."

    return output

print(sum_average(words))