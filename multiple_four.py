words = ["welter", "camelot", "abeng", "linsang", "pyogenic", "noctidiurnal", "portreeve", "wagtail", "woofits", "scammony", "nupson", "bulla", "plaustral", "cardimelech", "almuce", "trochiferous", "nullism"]

def reverse_four(array):
    reverse = [i[::-1] for i in array]
    fourArray = []
    for x in reverse:
        if len(x) % 4 == 0:
            fourArray.append(x)
    return fourArray

print(reverse_four(words))