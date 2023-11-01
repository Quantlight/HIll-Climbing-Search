from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.97'
DESCRIPTION = 'Implementation of Hill Climbing Search Based on 2d Vectors'

# Setting up
setup(
    name="Hill Climbing Search",
    version=VERSION,
    author="Quantity Light",
    author_email="lightquantity@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'random', 'networkx'],
    keywords=['python', 'hill', 'climbing', 'hill climbing', 'search', 'hill climbing search'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)