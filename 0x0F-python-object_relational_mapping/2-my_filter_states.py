#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
       print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
       sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try: 
       db = MySQLdb.connect(host="localhost", user="root", passwd="grace@07", port=3306, database="hbtn_0e_0_usa")

       cur = db.cursor()
       query = "SELECT * from states WHERE name = '{}' ORDER BY id ASC".format(state_name)
       cur.execute(query)
       rows = cur.fetchall()

       for row in rows:
           print(row)

       cur.close()
       db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
