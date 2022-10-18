import random
list_of_num = [random.randint(0,200) for _ in range(101)]

print(list_of_num)

def first_second(num):
    first = 0
    second = 0

    for x in num:
        if x > first:
            second = first
            first = x
        elif x > second:
            second = x

    output = print(f"First number is {first}, and the second number is {second}")
    
    return output

first_second(list_of_num)