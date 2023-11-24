#!/usr/bin/python3
"""prints the State object with the name passed as argument
   from the database hbtn_0e_6_usa
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
    - sys.argv[4]: state name to search (SQL injection free)
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name ==
                                         state_name).first()

    if states is not None:
        print("{0}".format(states.id))
    else:
        print("Not found")
