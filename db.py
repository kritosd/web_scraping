
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Euromillions, Base

# Create an engine to connect to the MySQL database
engine = create_engine('mysql://root:123@mysql:3306/euromillions', echo=True)
# Create the tables in the database
Base.metadata.create_all(engine)
# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def add(data):
    # Add data to the session
    session.add(data)
    # Commit the session to save the changes to the database
    session.commit()
    # Close the session
    session.close()

# Check if a record exists for a given draw_number
def record_exists(draw_number):
    record = session.query(Euromillions).filter_by(draw_number=draw_number).first()
    return record is not None

# Function to update a record by draw_number
def update_record(draw_number, data):
    # Query the record by draw_number
    record = session.query(Euromillions).filter_by(draw_number=draw_number).first()

    if record:
        valid_attributes = vars(Euromillions)

        for key, value in vars(data).items():
            # Check if the key exists as an attribute in the Euromillions model
            if key in valid_attributes:
                setattr(record, key, value)
            else:
                print(f"Attribute {key} does not exist in Euromillions model.")

        # Commit the changes
        session.commit()
        print(f"Record with draw_number {draw_number} has been successfully updated.")
    else:
        print(f"No record found with draw_number {draw_number}.")
