#in these we try to conver the data into the way we will use it for training purpose....... 
#handling missing values
#outlier treatment
#handle imbalance dataset
#convert categorical columns in numerical columns
#taking data from the jupyter notebook which is already done fe and convert categorical data into numerical col
import os,sys
import numpy as np
import pandas as pd
from source.logger import logging
from source.exception import CustomException
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from source.utils import save_object

@dataclass #decorator
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("Artifacts/data_transformation","preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfiguration()

    def get_data_transformation_obj(self):
        try:
            logging.info("Data Transformation Started")
            #copying data from numerical feature jupternotebook
            numerical_features = ['age', 'workclass', 'education_num', 'marital_status', 'occupation',
                                    'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
                                    'hours_per_week', 'native_country']
            

            num_pipeline = Pipeline(
                steps=[(
                    "imputer", SimpleImputer(strategy='median')),
                    ("scaler", StandardScaler())
                ]
            )

            #if we have categorical pipeline
            '''
            cat_pipeline = Pipeline(
                steps=[
                    ('onehot', OneHotEncoder()),
                    ('imputer',SimpleImputer(strategy='mode')),
                ]
            )
            '''

            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_features)
            ])

            return preprocessor


            
        except Exception as e:
            logging.info('error occured at data_transformation')
            raise CustomException(e, sys)

    #now we handle outliers
    def remove_outliers(self,col,df):
        try:
            Q1 = df[col].quartile(0.25)
            Q3 = df[col].quartile(0.75)
            IQR = Q3 - Q1
            #defining upper limit and lower limit
            upper_limit = Q3 + 1.5(IQR)
            lower_limit = Q1 - 1.5(IQR)

            df.loc[(df[col]>upper_limit), col] = upper_limit
            df.loc[(df[col]<lower_limit), col] = lower_limit

            return df


        except Exception as e:
            logging.info('treating outliers')
            raise CustomException(e,sys)

    def inititate_data_transformation(self, train_path, test_path):

        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            numerical_features = ['age', 'workclass', 'education_num', 'marital_status', 'occupation',
                                    'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
                                    'hours_per_week', 'native_country']
            
            #looping through items to remove outliers

            for col in numerical_features:
                self.remove_outliers(col=col, df = train_data)

            logging.info("removing outliers for train data")



            for col in numerical_features:
                self.remove_outliers(col=col, df = test_data)

            logging.info("removing outliers for test data")

            preprocess_obj = self.get_data_transformation_obj()

            target_column = "income"
            drop_column =[target_column]

            #splitting the data into independent and dependent features
            logging.info("splitting the data into independent and dependent features for train data")
            input_feature_train_data = train_data.drop(drop_column, axis=1)
            target_feature_train_data = train_data[target_column]

            logging.info("splitting the data into independent and dependent features for test data")
            input_feature_test_data = test_data.drop(drop_column, axis=1)
            target_feature_test_data = test_data[target_column]

            #apply transformation on our train data and test data.. 
            input_train_arr = preprocess_obj.fit_transform(input_feature_train_data)
            input_test_arr = preprocess_obj.transform(input_feature_test_data)

            #apply preprocessor obj on our train and test data
            #np.c_ means concatenate the data
            train_array = np.c_[input_train_arr, np.array(traget_feature_train_data)]
            test_array = np.c_[input_test_arr, np.array(traget_feature_test_data)]


            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocess_obj)

            return (train_array, test_array,
            self.data_transformation_config.preprocessor_obj_file_path)




        

        



        except Exception as e:
            logging.info('Initiate Data transformation technique')
            raise CustomException(e,sys)