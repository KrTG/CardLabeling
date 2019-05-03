# Decription
A website that was made to label cards to make a labeled training set of card corners for the
PokerHandDetection project. I've since found better way to gather the data so it doesn't have to be labeled
like this.

# Installation
Install pipenv
C: > pip install pipenv

Install dependencies from Pipfile
C: > pipenv install

Start the pipenv shell:
C: > pipenv shell

Alternatively, the dependencies listed in Pipfile can be installed manually into a conda or virtualenv
environment.

.env file has to be modified with the correct database URL (engine://user:passwordg@address/database)