#!/usr/bin/python3
'''
    A script that list's a passed param state id
    from a database provided with search param
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_states(username, pwd, database):
    '''
        List all State object from the specified database
    '''
    # Create the engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
            @localhost:3306/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects with their corresponding City objects
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'    {city.id}: {city.name}')

    # Close the session
    session.close()


if __name__ == '__main__':
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python 100-relationship_states_cities.py \
                <username> <password> <database>")
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
