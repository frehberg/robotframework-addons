from setuptools import setup, find_packages

with open('README.md') as file:
    long_description = file.read()

setup(
    name = "robotframeworkplus",
    version = "0.2",
    py_modules = ['lib/RobotChart', 'lib/RobotProcessEx'],
    setup_requires = ["svg.charts >= 2.2" ],
    author = "Frank Rehberger",
    author_email = "frehberg@gmail.com",
    description = "This is a Toolset adding new functionalities to  RobotFramework, such as embedding chart diagrams or improved process management",
    license = "Apache License",
    url = "https://github.com/frehberg/robotframeworkplus",
    long_description=long_description)