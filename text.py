from source.exception import CustomException
from source.logger import logging
import os,sys
a=int(input("enter a number: "))
b=int(input('enter the second number: '))
logging.info("Entered the two number")
try:
    c=a/b
    print(c) 


except Exception as e:
    raise CustomException(e,sys)