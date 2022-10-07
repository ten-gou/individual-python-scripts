#numbers array
numbers = [8,6,9,1,3,1,5,10,469]

#inits the even/odd variables
even = 0
odd = 0

#adds +1 to even/odd depending on if it is divisible by 2
for x in numbers:
    if x % 2 == 0:
        even += 1
    elif x % 2 == 1:
        odd += 1

#prints output
print(f'Of the numbers array, there are {even} even numbers and {odd} odd numbers')