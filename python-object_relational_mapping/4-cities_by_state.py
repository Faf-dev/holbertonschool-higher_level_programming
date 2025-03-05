#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("usage : ./<script.py> <username> <password> <database_name>")
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
        cursor.execute("SELECT cities.id, cities.name, states.name  \
                       FROM cities JOIN states \
                       ON cities.state_id = states.id \
                       ORDER BY cities.id ASC;")

        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Connexion to database failed : {e}")
        sys.exit(1)
