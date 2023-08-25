#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    
    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database_name))
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Retrieve all State objects and sort by states.id in ascending order
    state = session.query(State).order_by(State.id).first()
    
    # Display the results
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    
    # Close the session
    session.close()
