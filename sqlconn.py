__author__ = 'bernardo'

import sqlite3 as lite

con = lite.connect('test.db')
con.row_factory = lite.Row



class entity:
    pass
"""
aa.uu = 11
vars(aa)['ca'] = 332

print vars(aa)
"""
if __name__ == "__main__":
    print 4543543