# Library to configure this setup file
from distutils.core import setup

# Import the version of the the family_birthdays
from family_birthdays import version as current_version
print("Current Library Version:", current_version)

# Use the README for the long description
long_description=open('README.rst').read() ### Change the content of README.rst

setup(
    name='family_birthdays',        ### Change here
    version=current_version,
    author='Sebastian Flores Benner',       ### Change here
    author_email='sebastiandres@gmail.com', ### Change here
    packages=['family_birthdays'],  ### Change here
    scripts=[],
    url='https://github.com/sebastiandres/family_birthdays',    ### Change here
    license='MIT',  ### May/May not change this. But if you change it, must also change LICENCE file
    description='A simple but functional interface for simulation code.', ### Change here
    long_description=long_description,
)