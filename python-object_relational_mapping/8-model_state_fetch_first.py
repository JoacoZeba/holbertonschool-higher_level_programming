#!/usr/bin/python3
"""
Module to retrieve and print the State object with id=1 from a MySQL database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    av = sys.argv[1:]
    engine = create_engine(
        f"mysql+mysqldb://{av[0]}:{av[1]}@localhost:3306/{av[2]}",
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 1).one_or_none()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
