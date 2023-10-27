import pandas as pd 
import numpy as np 
import os, sys
from source.logger import logging
from source.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from source.components.data_transformation import DataTransformation
#main puprose of these file is to collect data from different types of souces

@dataclass
class DataIngestionConfig:
    #he we write the code for data ingestion it can be from different types of souces that code will be writtenhere
    train_data_path = os.path.join('Artifacts', 'train.csv')
    test_data_path = os.path.join('Artifacts','test.csv')
    raw_data_path = os.path.join('Artifacts', 'raw.csv')
    logging.info('created file paths for train, test & raw') 


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('data ingestion started')
        try:
            logging.info('reading the data using pandas library from local system')
            #data = pd.read_csv('notebook\data\adult.csv')#copy relative path
            data = pd.read_csv(os.path.join('notebook/data', 'adult.csv'))
            logging.info('reading the data is completed')
            #creating folder for artifact
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('splitting data into train and test')

            train_set, test_set = train_test_split(data, test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header = True)

            logging.info(' data ingestion completd')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info('error occured in data ingestion')
            raise CustomException(e, sys)

'''
below code is for only data transformation
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
'''
if __name__ =="__main__":
    obj = DataIngestion()
    train_data_path , test_data_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.inititate_data_transformation(train_data_path , test_data_path)




#python source\components\data_ingestion.py
