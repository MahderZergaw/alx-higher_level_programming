#!/usr/bin/python3
""" lists the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to a MySQL server

    Args:
    - sys.argv[1]: MySQL username
    - sys.argv[2]: MySQL password
    - sys.argv[3]: Name of the database containing the states table
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()

    if states is not None:
        print("{0}: {1}".format(states.id, states.name))
    else:
        print("Nothing")
