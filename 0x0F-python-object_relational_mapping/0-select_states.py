#!/usr/bin/python3
""" 
    list all the data
    from a SQL database
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for n in cursor:
        all = str(n)
        print("%s " % all)
    db.close()
