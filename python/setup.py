import os
from setuptools import setup, find_packages

#from ez_setup import use_setuptools
#use_setuptools()

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "DFXML Python Tools",
    version = "1.1.0",
    author = "DFXML",
    author_email = "dfxml@dfxml.com",
    description = ("Initial DFXML setuptools."),
    license = "Public Domain",
    keywords = "DFXML python",
    url = "https://github.com/simsong/dfxml",
    packages=['dfxml', 'test'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: Public Domain",
    ],
)

