#!/usr/bin/python3
"""
Take in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("Usage : ./<script.py> <username> \
              <password> <databse_name> <state_name>")
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
        cursor.execute("SELECT cities.name FROM cities \
                       JOIN states on states.id = cities.state_id \
                       WHERE states.name = %s \
                       ORDER BY cities.id ASC;", (state_name,))
        result = cursor.fetchall()
        result_string = ", ".join([row[0] for row in result])
        print(result_string)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Connexion to database failed : {e}")
        sys.exit(1)
