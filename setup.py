from setuptools import setup
from typing import List

#Declaring Variable for Project
PROJECT_NAME= "housing-predictor"
VERSION="0.0.1"
AUTHOR="Pranay"
DESCRIPTION="This is a first FSDS Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    description : This function is going to return list of requirements
    mention in requirements.txt file

    return this function is going to return a list which contain name
    of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)



