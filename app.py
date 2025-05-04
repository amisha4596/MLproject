from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
import sys
from src.components.data_ingestion import DataIngestionConfig
if __name__ == "__main__":
    logging.info("The execution has started")  # Ensure this logs in terminal
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.error(f"Custom Exception: {str(e)}")  # Change to logging.error to show errors in the terminal
        raise CustomException(e, sys)
