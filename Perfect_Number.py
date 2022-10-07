#input number value
print('Enter a number: ')
number = input()
while number.isdecimal() == False: #reruns the input until a number is received
    print('Incorrect input! Please input a number!')
    number = input()
print('You inputted ' + number + "! Now let's see if this number is Perfect!")

#sets up the array for the divisors
divisors = []
divider = 1

#remains in effect as long as divider is less than the number
while divider < int(number):
    if int(number) % divider == 0:
        divisors.append(divider) #adds the divder to the array if the remainder is equal to 0
    divider += 1

#creates a sum for the array to be added into
sum = 0
for x in divisors:
    sum += x

#returns the list of divisors
print('This number has the following divisors: ' + str(divisors) + ' for a total of ' + str(sum))

#checks to see if they match
check = int(number) == sum

#output
print('Is the number ' + number + ' perfect? ' + str(check))