#!/usr/bin/python3
"""
Same as task 2 and counter sql injection
"""
import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("usage: ./<script.py> <username> <password> \
              <database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    user_password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=user_password,
            db=database
        )
        cursor = db.cursor()
        cursor.execute("SELECT id, name FROM states WHERE name = %s \
                       ORDER BY states.id ASC;"(state_name,))

        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Connexion to database failed : {e}")
        sys.exit(1)
