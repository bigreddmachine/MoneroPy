import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "moneropy",
    version = "0.0.1",
    description = "A python toolbox for Monero.",
    long_description=read('README.md'),
    url = "https://github.com/monero-monitor/moneropy",
    keywords = "monero",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD 3-Clause License"
    ],
    license = "BSD-3-Clause"
)
