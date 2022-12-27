#!/usr/bin/python3
"""
A script that deletes all State objects with
charater a in its name from the database
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
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    if states is not None:
        for state in states:
            session.delete(state)

    session.commit()

    session.close()
