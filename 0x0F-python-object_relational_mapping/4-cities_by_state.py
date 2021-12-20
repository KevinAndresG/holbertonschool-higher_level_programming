#!/usr/bin/python3
"""
    list all cities
    from database
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])

    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")

    justN = curs.fetchall()
    for n in justN:
        print(n)

    db.close()
