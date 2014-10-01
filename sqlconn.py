__author__ = 'bernardo'

import sqlite3 as lite



con = None

def connect(filename):
    global con
    con = lite.connect(filename)
    con.row_factory = lite.Row

def readTable(tableName, where = ""):


class entity:
    pass




"""
aa.uu = 11
vars(aa)['ca'] = 332

print vars(aa)
"""
if __name__ == "__main__":
