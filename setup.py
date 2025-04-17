from setuptools import find_packages, setup
from typing import List

HYPEN_e_dot='-e .'
def getrequirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        if HYPEN_e_dot in requirement:
            requirement.remove(HYPEN_e_dot)
    return requirement
setup(
    name='mlproject',
    version='0.0.1',
    author='Swayam',
    author_email='kambleswayam15@gmail.com',
    packages=find_packages(),
    install_requires=getrequirements('requirements.txt')
)