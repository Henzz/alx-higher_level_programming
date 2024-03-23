#!/usr/bin/python3
'''
    A script that lists all states from a database provided
    with search param
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, pwd, database):
    '''
        List all State object from the specified database
    '''
    # Create the engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    session = sessionmaker(bind=engine)
    session = session()

    # Query the State objects from the database and sort by id
    states = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == '__main__':
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py \
                <username> <password> <database> <state>")
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
