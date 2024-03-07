ogRange = [[3,9],
[6,10],
[2,8],
[12,6],
[18,24],
[16,20],
[0,2],
[12,14],
[18,26],
[30,33],
[31,32],
[33,39]
]

interRange = []
mergedRange = []

def sort(range):
    range.sort()
    return range

def inbetween(input,ranger):
    if len(ranger) == 0:
        ranger.append(input)

    overlap = True

    for x in ranger:
        if x[0] > input[0] and input[1] <= x[1] and input[1] >= x[0]:
            x[0] = input[0]
        elif x[1] < input[1] and input[0] <= x[1] and input[0] >= x[0]:
            x[1] = input[1]
    
    for x in ranger:
        if input[0] > x[1] and input[1] > x[1]:
            overlap = False
        elif input[0] < x[0] and input[1] < x[1]:
            overlap = False
        else:
            overlap = True
            break
    
    if overlap == False:
        ranger.append(input)

for x in ogRange:
    sort(x)
    inbetween(x, interRange)

for x in interRange:
    inbetween(x, mergedRange)

print(f"{interRange}")
print(f"{mergedRange}")