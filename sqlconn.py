__author__ = 'bernardo'

import sqlite3 as lite

con = None

class entity:
    _tableName = ""
    def buildEntity(self, table):
        global con
        cur = con.cursor()
        cur.execute("pragma table_info('"+table+"')")
        rows = cur.fetchall()
        for x in range(0, len(rows)):

            vars(self)[rows[x][(1)]] = None
        self._tableName = table
        return self

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
        rox._tableName = tableName
        dataset.append(rox)

    return dataset

def writeTable(entity, tableName=entity._tableName):
    global con
    cur = con.cursor()
    fields = ""
    values = ""


    for _ in xrange(0, len(vars(entity).keys())):
        if str(vars(entity).keys()[_]).startswith("_") == False:
            fields += str(vars(entity).keys()[_]) + ","
            values += "'"+str(vars(entity).values()[_])+"'"+","

    strs = "INSERT INTO "+tableName+" ("+fields[:-1]+") VALUES ("+values+")"
    print strs
    cur.execute(strs)
    affectedRows = cur.rowcount
    if affectedRows >= 1:
        print "OK"




"""
aa.uu = 11
vars(aa)['ca'] = 332

print vars(aa)
"""
if __name__ == "__main__":
    connect("test.db")
    #datase = readTable("Users")
    #print vars(datase[1])

    x = entity()
    x.buildEntity("Users")
    x.login = "connnn"
    x.password = "connnn"

    writeTable(x)
