from datetime import datetime

class UsageData:
    date = ""
    power = -1.0
    coldWater = -1.0
    warmWater = -1.0

    def parseRow(self, row ):
        self.date = datetime.strptime(row[1], '%d:%m:%Y')
        self.power = float(row[2])
        self.coldWater = float(row[3])
        self.warmWater = float(row[4])

    def __init__(self, row):
        self.parseRow(row)
