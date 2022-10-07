#input
human_age = float(input("Enter a dog's age in human years: "))

#checks if invalid input
if human_age <= 0:
    convert_dog_age = 0
else:
    #conversion equation
    convert_dog_age = ((human_age - 1) * 4) + 10.5

#output
print(f"The dog's age in dog years is {convert_dog_age}")