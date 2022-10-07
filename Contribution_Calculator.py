#input salary
print('Enter monthly salary:')
inputSalary = input()
if inputSalary.isdecimal() == True:
    intSalary = int(inputSalary)

#input age
print('Enter your Age:')
inputAge = input()
if inputAge.isdecimal() == True:
    intAge = int(inputAge)

#check inputs
print('You entered $' + inputSalary + ' for the salary and you entered ' + inputAge + ' for your age')

#array table for contribution %s
contribution = [
    {
        'age': 55,
        'employee': 20,
        'employer': 17
    },
    {
        'age': 60,
        'employee': 13,
        'employer': 13
    },
    {
        'age': 65,
        'employee': 7.5,
        'employer': 9
    },
    {
        'age': intAge + 1,
        'employee': 5,
        'employer': 7.5
    },
]

#stops the program if it detects invalid inputs
if inputSalary.isdecimal() == False or inputAge.isdecimal() == False:
    print('Invalid prompt detected!')
else:
    #runs through the array's ages
    for x in contribution:
        #contribution.index(x) tracks value of the array the fxn is on
        if intAge <= x['age']: #when input age is less than array age, stops the fxn
            break

    #math calculation to determine contribution amounts
    employeeC = intSalary * contribution[contribution.index(x)]['employee']/100
    employerC = intSalary * contribution[contribution.index(x)]['employer']/100
    totalC = employeeC + employerC

    #returns values as output string
    print('Employee: contributes $' + str(employeeC) + ' at a rate of ' + str(contribution[contribution.index(x)]['employee']) + '%, Employer: contributes $' + str(employerC) + ' at a rate of ' + str(contribution[contribution.index(x)]['employer']) + '%.')
    print('The total contribution is: $' + str(totalC))
