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
    curs.execute("""SELECT cities.name FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name= '{}'
                ORDER BY cities.id ASC""".format(sys.argv[4]))

    justN = curs.fetchall()
    k = 0
    t = len(justN) - 1
    for n in justN:
        print(n[0], end="")
        if k < t:
            print(', ', end="")
            k += 1
    print('')
    db.close()
