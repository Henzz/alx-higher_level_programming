#!/usr/bin/python3
'''
    A script that list's a passed param state id
    from a database provided with search param
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

    # Create a new State object
    new_state = State(name='Louisiana')

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to persist the changes to the database
    session.commit()

    # Display the new state's id
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == '__main__':
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py \
                <username> <password> <database>")
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
