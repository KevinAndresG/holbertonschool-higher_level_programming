#!/usr/bin/python3
"""list all states from database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    curs = db.cursor()

    curs.execute("SELECT * FROM states ORDER BY id ASC")
    for x in curs:
        data = str(x)
        print("%s " % data)

    db.close()
