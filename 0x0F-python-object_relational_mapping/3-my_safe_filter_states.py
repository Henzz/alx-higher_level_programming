#!/usr/bin/python3
'''
    A script that lists all states from a database provided
    with search param
'''
import MySQLdb
import sys


def list_states(username, pwd, database, search):
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
    cur.execute("""SELECT * FROM states WHERE BINARY name = %(search)s \
            ORDER BY id ASC""", {'search': search})

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()


if __name__ == '__main__':
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py \
                <username> <password> <database> <search>")
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    list_states(username, password, database, search)
