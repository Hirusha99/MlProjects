'''
End to end ML project - setup.py
'''
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:  # this will return a list
    '''
    this function will returns the list of reuirements
    '''
    requirements = []
    # let create this as a tempory object file object
    with open(file_path, encoding="utf-8") as file_obj:
        requirements = file_obj.readlines()  # read line by line in requirements.txt file
        requirements = [req.replace("\n", "")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Hirusha",
    author_email="hirushanethni2277@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
