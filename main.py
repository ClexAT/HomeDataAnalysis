from datetime import date
from UsageData import UsageData
import Database as db
import matplotlib.pyplot as plt


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

        print("Data added successfully!")

        inp = askMenu()

    while (inp == 2):
        print("Reading all Data")
        data = db.readAll()
        cwData = [x for x in data if x.coldWater != -1.0]
        wwData = [x for x in data if x.warmWater != -1.0]
        pwData = [x for x in data if x.power != -1.0]

        plt.subplot(1, 3, 1)
        plt.plot([x.date for x in cwData], [x.coldWater for x in cwData], marker="x", linestyle="None")
        plt.subplot(1, 3, 2)
        plt.plot([x.date for x in wwData], [x.warmWater for x in wwData], marker="x", linestyle="None")
        plt.subplot(1, 3, 3)
        plt.plot([x.date for x in pwData], [x.power for x in pwData], marker="x", linestyle="None")
        plt.show()

        inp = askMenu()


else:
    print("Wrong Input or Exit, Goodbye!")