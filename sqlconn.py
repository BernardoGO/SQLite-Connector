__author__ = 'bernardo'

import sqlite3 as lite


class entity:
    pass

con = None

def connect(filename):
    global con
    con = lite.connect(filename)
    con.row_factory = lite.Row

def readTable(tableName, where = ""):
    global con
    cur = con.cursor()
    cur.execute("SELECT * FROM " + tableName)
    rows = cur.fetchall()

    dataset = []

    for x in rows:
        rox = entity()
        vars(rox)[] x['Id']





"""
aa.uu = 11
vars(aa)['ca'] = 332

print vars(aa)
"""
if __name__ == "__main__":
    connect("test")