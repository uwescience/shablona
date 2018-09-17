#!/usr/bin/env bash

echo "Checking git and conda"
git --version
if [ $? -ne 0 ]
then
    echo "Error!  Git is not installed!"
fi

conda --version
if [ $? -ne 0 ]
then
    echo "Error!  Anaconda is not installed!"
fi

echo "Checking Python version"
python --version
if [ $? -ne 0 ]
then
    echo "Error!  Python is not installed, which probably means that Anaconda did not install correctly!"
fi

echo "Checking Python packages ..."
python -c "import flake8"
if [ $? -ne 0 ]
then
    echo "Error!  You're missing flake8, a Python package."
fi

python -c "import jupyter"
if [ $? -ne 0 ]
then
    echo "Error!  You're missing jupyter, a Python package."
fi

python -c "import matplotlib"
if [ $? -ne 0 ]
then
    echo "Error!  You're missing matplotlib, a Python package."
fi

python -c "import numpy"
if [ $? -ne 0 ]
then
    echo "Error!  You're missing numpy, a Python package."
fi

python -c "import scipy"
if [ $? -ne 0 ]
then
    echo "Error!  You're missing scipy, a Python package."
fi

python -c "import sklearn"
if [ $? -ne 0 ]
then
    echo "Error!  You're missing sklearn, a Python package."
fi

python -c "import sphinx"
if [ $? -ne 0 ]
then
    echo "Error!  You're missing sphinx, a Python package."
fi

echo "Success! Everything appears to be installed!"
