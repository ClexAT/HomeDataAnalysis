import sqlite3
from datetime import datetime

from UsageData import UsageData


def add(data : UsageData):
    con = sqlite3.connect("sqlite/Database/homeusage.db")
    cur = con.cursor()
    con.execute("INSERT INTO UsageData (Date, Power, ColdWater, WarmWater) VALUES (?, ?, ?, ?)",
                (data.date, data.power, data.coldWater, data.warmWater))
    con.commit()
    con.close()

def readAll():
    con = sqlite3.connect("sqlite/Database/homeusage.db")
    cur = con.cursor()
    data = []
    for row in con.execute("select * from UsageData"):
        data.append(UsageData(row))

    data.sort(key=lambda x: x.date, reverse=True)
    return data



