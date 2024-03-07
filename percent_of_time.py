import math

def main():
    timeSpent = input("How much time did you spend on the test? Input in mm:ss format please!\n")

    while ":" not in timeSpent or timeSpent.split(":")[0].isdigit() == False or timeSpent.split(":")[1].isdigit() == False:
        timeSpent = input("How much time did you spend on the test? Input in mm:ss format please!\n")

    minute = int(timeSpent.split(":")[0])
    second = int(timeSpent.split(":")[1])

    totalTime = (minute * 60) + second

    score = input("What score did you receive?\n")

    while score.isdigit() == False:
        score = input("What score did you receive?")

    score = int(score)
    totalOff = (totalTime*score)/100

    minuteOff = math.trunc(totalOff // 60)
    secondOff = math.trunc(totalOff - (minuteOff * 60))

    if (secondOff >= 10):
        print(f"{minuteOff}:{secondOff}")
    else:
        print(f"{minuteOff}:0{secondOff}")
    
    main()

main()