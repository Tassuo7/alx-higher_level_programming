#!/usr/bin/python3
"""takes in arguments
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, safe from MySQL injections!"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    msafe = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (msafe, ))
    states = cur.fetchall()
    for stt in states:
        print(stt)
    cur.close()
    db.close()
