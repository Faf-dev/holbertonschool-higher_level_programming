#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    user_password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=user_password,
            db=database
        )
        cursor = db.cursor()
        cursor.execute("SELECT id, name FROM states WHERE name LIKE \
                       'N%' ORDER BY states.id ASC;")

        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Connexion to database failed : {e}")
        sys.exit(1)
