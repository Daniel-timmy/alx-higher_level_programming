#!/usr/bin/python3
"""
A script that lists all State objects from the database
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to get the states from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session =Session()
    states = session.query(State).order_by(State.id)

    for state in states:
        print('{}: {}'.format(state.id, state.name))
