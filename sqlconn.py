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
    fieldnames=[f[0] for f in cur.description]
    dataset = []

    for x in range(0, len(rows)):
        rox = entity()
        for y in range(0, len(fieldnames)):
            vars(rox)[fieldnames[y]] = rows[x][str(fieldnames[y])]

        dataset.append(rox)


    return dataset


"""
aa.uu = 11
vars(aa)['ca'] = 332

print vars(aa)
"""
if __name__ == "__main__":
    connect("test.db")
    datase = readTable("Users")
    print vars(datase[0])