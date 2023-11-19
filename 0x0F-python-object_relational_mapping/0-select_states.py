#!/usr/bin/python3
"""
    ascript that  lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3]) 
mycursor = db.cursor()
mycursor.execute("SELECT * FROM states")
row = mycursor.fetchall()

for row in mycursor:
    print(row)

mycursor.close()
db.close()
