import sqlite3

from UsageData import UsageData


def add(data : UsageData):
    con = sqlite3.connect("sqlite/Database/homeusage.db")
    cur = con.cursor()
    con.execute("INSERT INTO UsageData (Date, Power, ColdWater, WarmWater) VALUES (?, ?, ?, ?)",
                (data.date, data.power, data.coldWater, data.warmWater))
    con.commit()
    con.close()

