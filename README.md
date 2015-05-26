# shablona

[![Coverage Status](https://coveralls.io/repos/arokem/shablona/badge.svg)](https://coveralls.io/r/arokem/shablona)

Shablona is a template project for small scientific python projects. To use it as a template for your own project, you will need to clone this repository into your computer and follow the instructions at the bottom of this page. First, let me explain all the different moving parts that make up a small scientific python project, and allow us to effectively share it with others, test it, document it, and track its evolution.

For the purpose of this explanation, I will assume that you know how to use git and github (if you don't, take a look at XXX Need some good git/github for science tutorial here!).



## Organization of the  project

The project has the following structure: 

	shablona -
			  |- `README.md`
				|- shablona
					|- `__init__.py`
					|- `shablona.py`
					|- data
						|- ...
					|- tests
						|- ...
			  |- doc
					|- `Makefile`
					|- `conf.py`
					|- sphinxext
						|- ...
					|- _static
						|- ...
			  |- `setup.py`
			  |- `.travis.yml`
			  |- `LICENSE`
			  |- ipynb
		  			|- ...


In the following sections we will examine these elements one by one. First, let's consider the core of the project. This is the code inside of `shablona/shablona.py`. This code is intentionally rather simple.

It's not too important to know what it does, but if you are really interested, you can read all about it [here](http//arokem.github.io/2014-08-12-learn-optimization.html)


## Module code


## Project Data
In this case, the project data is rather small, and recorded in csv files. Thus, it can be stored alongside the module code. Even if the data that you are analyzing is too large, and cannot be effectively tracked with github, you might still want to store some data for testing purposes. 

## Testing 


## Documentation 


## Installation

For installation and distribution we will use the python standard library `distutils` module. This module uses a `setup.py` file to 

Much more information on packaging Python software can be found in the [Hitchhiker's guide to packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.org).


## Continuous integration

Travis-CI is a system that can be used to automatically test every revision of your code directly from github, including testing of github pull requests, before they are merged into the `master` branch. This provides you with information needed in order to evaluate contrubutions made by others. It also serves as a source of information for others interested in using or contributing to your project about the degree of test coverage of your project. 

You will need a .travis.yml file. This file contains the 

You will need to go to the Travis-CI [website]()

## Distribution

## Licensing

License your code! A repository like this without a license is legally closed-source and cannot be used by others. Follow Jake's [advice](http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/)!

## Scripts 
A scripts directory can be used as a place to experiment with your module code, and as a place to produce scripts that contain a narrative structure, demonstrating the use of the code, or producing scientific results from your code and your data and telling a story with these elements.
