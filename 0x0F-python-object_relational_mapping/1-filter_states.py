#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
       print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
       sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try: 
       db = MySQLdb.connect(host="localhost", user="root", passwd="root", port=3306, database="hbtn_0e_0_usa")

       cur = db.cursor()
       cur.execute("SELECT * from states WHERE name LIKE 'N%' ORDER BY id ASC")
       rows = cur.fetchall()

       for row in rows:
           print(row)

       cur.close()
       db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
