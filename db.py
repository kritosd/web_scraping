
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Euromillions, Base

def add(data):
    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql://root:123@mysql:3306/euromillions', echo=True)
    # Create the tables in the database
    Base.metadata.create_all(engine)
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    # Add data to the session
    session.add(data)
    # Commit the session to save the changes to the database
    session.commit()
    # Close the session
    session.close()
