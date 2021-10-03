from datetime import date
from UsageData import UsageData
import Database as db


def askMenu():
    print("Hi, do you wish to add (1) or read data (2).")
    print("You can also exit (0)")
    return int(input("Input: "))

inp = askMenu()

while(inp != 0):

    while (inp == 1):
        data = UsageData()
        print("Enter the Date as DD:MM:YYYY")
        data.date = input("Input: ")
        print("Input Power Usage as x.x")
        data.power = float(input("Input: "))
        print("Input Cold Water Usage as x.x")
        data.coldWater = float(input("Input: "))
        print("Input Warm Water Usage as x.x")
        data.warmWater = float(input("Input: "))

        db.add(data)

        print("Data added sucessfully!")

        inp = askMenu()


    while (inp == 2):
        pass

else:
    print("Wrong Input or Exit, Goodbye!")