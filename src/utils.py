import os
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv('db')


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connection Established: {mydb}")
        
        # Read data from 'students' table
        df = pd.read_sql_query('SELECT * FROM students', mydb)
        
        # Log the shape of the dataframe (e.g., number of rows and columns)
        logging.info(f"Data retrieved with {df.shape[0]} rows and {df.shape[1]} columns.")
        
        # Close the database connection
        mydb.close()
        logging.info("Database connection closed.")
        
        # Optionally, print the first few rows of the dataframe
        print(df.head())

        return df

    except Exception as ex:
        logging.error(f"Error occurred: {str(ex)}")
        raise CustomException(ex, sys)
