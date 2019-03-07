Installation
Using PIP via PyPI

pip install fuzzywuzzy

or the following to install python-Levenshtein too

pip install fuzzywuzzy[speedup]

Using PIP via Github

pip install git+git://github.com/seatgeek/fuzzywuzzy.git@0.17.0#egg=fuzzywuzzy

Adding to your requirements.txt file (run pip install -r requirements.txt afterwards)

git+ssh://git@github.com/seatgeek/fuzzywuzzy.git@0.17.0#egg=fuzzywuzzy

Manually via GIT

git clone git://github.com/seatgeek/fuzzywuzzy.git fuzzywuzzy
cd fuzzywuzzy
python setup.py install

Usage

>>> from fuzzywuzzy import fuzz
>>> from fuzzywuzzy import process
