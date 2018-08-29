echo "Checking git and conda"
git --version
conda --version
echo "\n"

echo "Checking python packages and python version"
python -c "import flake8"
python -c "import jupyter"
python -c "import matplotlib"
python -c "import numpy"
python -c "import pandas"
python -c "import requests"
python -c "import scipy"
python -c "import sklearn"
python -c "import sphinx"
python --version

echo "Success!"
