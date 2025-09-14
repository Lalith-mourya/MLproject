from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(filepath:str)->List[str]:
    """
    this function return the list of dependencies from the
    requirements.txt
    """
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="Mlproject",
    author="MOURYA",
    version='0.0.1',
    author_email='mouryalalith83@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)