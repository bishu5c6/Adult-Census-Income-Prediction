#here we are creating a helper function to save the data transformation file
from source.logger import logging
from source.exception import CustomException
import os,sys
import pickle

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        #creating a folder
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

#with the help of above function we are svaing the pickle file into artifacts pickle file