#!/usr/bin/python3
"""
    list all states
    that start with N
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    curs = db.cursor()

    curs.execute("""SELECT id, name FROM states
                WHERE Name LIKE BINARY 'N%' ORDER BY id ASC""")
    justN = curs.fetchall()
    for n in justN:
        print(n)

    db.close()
