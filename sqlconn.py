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

def readTable(tableName, whereEntity = None):
    global con
    cur = con.cursor()
    where = ""
    if whereEntity is not None:
        where += " WHERE "
        for _ in xrange(0, len(vars(whereEntity).keys())):
            if str(vars(whereEntity).keys()[_]).startswith("_") == False \
                    and (vars(whereEntity).values()[_] is not None):
                where += str(vars(whereEntity).keys()[_]) + " = '" + \
                         ""+str(vars(whereEntity).values()[_])+"'"+" and "

    strds = "SELECT * FROM " + tableName + where[:-5]
    print strds
    cur.execute(strds)

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

def writeTable(entity, tableName=""):
    global con
    cur = con.cursor()
    fields = ""
    values = ""
    if tableName == "": tableName = entity._tableName

    for _ in xrange(0, len(vars(entity).keys())):
        if str(vars(entity).keys()[_]).startswith("_") == False \
                and (vars(entity).values()[_] is not None):
            fields += str(vars(entity).keys()[_]) + ","
            values += "'"+str(vars(entity).values()[_])+"'"+","
    ax = lambda __:__[:-1];
    strs = "INSERT INTO "+tableName+" ("+ax(fields)+") VALUES ("+ax(values)+")"
    print strs
    cur.execute(strs)
    affectedRows = cur.rowcount
    if affectedRows >= 1:
        con.commit()
        print "OK"



if __name__ == "__main__":
    connect("test.db")


    x = entity()
    x.buildEntity("Users")
    x.login = "admin"
    x.password = "admin"

    #writeTable(x)
    datase = readTable("Users", x)
    for x in xrange(0, len(datase)): print vars(datase[x])