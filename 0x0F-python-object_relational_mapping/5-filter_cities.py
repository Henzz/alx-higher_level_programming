#!/usr/bin/python3
'''
    A script that lists all states from a database provided
    with search param
'''
import MySQLdb
import sys


def list_cities(username, pwd, database, state):
    '''
        Fetches data from database with search param
    '''
    # Connect to MySQL server
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=pwd,
            db=database)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute the SQL query to retrieve states
    cur.execute("""SELECT cities.name FROM cities LEFT JOIN states ON \
            states.id = cities.state_id WHERE BINARY states.name = %(state)s \
            ORDER BY cities.id ASC""", {'state': state})

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    i = len(rows)
    j = 1
    # Display the results
    for row in rows:
        if (j != i):
            print(row[0], end=", ")
        else:
            print(row[0], end="\n")
        j += 1

    if (i == 0):
        print()

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == '__main__':
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py \
                <username> <password> <database> <state>")
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    list_cities(username, password, database, state)
