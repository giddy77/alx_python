from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

# Define the SQLAlchemy model
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

def list_states(username, password, database_name):
    try:
        # Create a database connection
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database_name}")

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query all states and order by id
        states = session.query(State).order_by(State.id).all()

        # Display the results
        for state in states:
            print(state.id, state.name)

        # Close the session
        session.close()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)
