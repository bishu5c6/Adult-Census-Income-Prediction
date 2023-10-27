from setuptools import setup, find_packages
from typing import List

PROJECT_NAME ="ADULT_CENSUS_INCOME_PREDICTION"
VERSION = "0.0.1"
DESCRIPTION = "END TO END ML PROJECT"
AUTHOR = "BISWANTH PINNIKA"
AUTHOR_EMAIL = "pinnikabiswanth@gmail.com"

REQUIREMENTS_FILE_NAME = 'requirements.txt'

HYPHON_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requriment_file:
        requriment_list = requriment_file.readlines()
        requriment_list = [ requriment_name.replace("\n", "") for requriment_name in requriment_list]

        if HYPHON_E_DOT in requriment_list:
            requriment_list.remove(HYPHON_E_DOT)
        return requriment_list


setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements_list()
     )