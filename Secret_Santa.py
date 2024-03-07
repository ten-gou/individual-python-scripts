import random

recipient = ['a', 'b', 'c','d','e']
gifter = ['a', 'b', 'c', 'd', 'e']

for x in recipient:
    if len(gifter) > 1:
        y = random.randint(0, len(gifter)-1)
        while x == gifter[y]:
            y = random.randint(0, len(gifter)-1)
    else:
        y = 0
    print(f"{x} will be the recipient of {gifter[y]}'s gift")
    gifter.pop(y)