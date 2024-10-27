
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base

# Create an engine to connect to the MySQL database
engine = create_engine('mysql://root:123@mysql:3306/games', echo=True)
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

# Check if a record exists for a given filter
def record_exists(filterColumn, filterMatch, Model):
    record = session.query(Model).filter_by(**{filterColumn: filterMatch}).first()
    return record is not None

# Function to update a record by filter
def update_record(filterColumn, filterMatch, data, Model):
    # Query the record by filter
    record = session.query(Model).filter_by(**{filterColumn: filterMatch}).first()
    print('update_reeeee')
    if record:
        valid_attributes = vars(Model)

        for key, value in vars(data).items():
            print(value)
            # Check if the key exists as an attribute in the model
            if key in valid_attributes:
                setattr(record, key, value)
            else:
                print(f"Attribute {key} does not exist in model.")

        # Commit the changes
        session.commit()
        print(f"Record with {filterColumn} {filterMatch} has been successfully updated.")
    else:
        print(f"No record found with {filterColumn} {filterMatch}.")
