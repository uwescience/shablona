# shablona

[![Coverage Status](https://coveralls.io/repos/arokem/shablona/badge.svg)](https://coveralls.io/r/arokem/shablona)

Shablona is a template project for small scientific python projects. To use it as a template for your own project, you will need to clone this repository into your computer and follow the instructions at the bottom of this page.

First, let me explain all the different moving parts that make up a small scientific python project, and which allow us to effectively share it with others, test it, document it, and track its evolution.

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

We place the module code in a file called `shablona.py` in directory called `shablona`. This structure is a bit confusing at first, but it is a simple way to create a structure where when we type `import shablona as sb` the classes and functions defined inside of the `shablona.py` file are available in the `sb` namespace. For this to work, we need to also create a file in `__init__.py` which contains code that imports everything in that file into the namespace of the project: 

    from .shablona import *

We follow the convention that a function is defined in lines that precede the lines that use that function. This helps readability of the code, because you know that if you see some name, the definition of that name will appear earlier in the file, either as a function/variable definition, or as an import from some other module or package.

In the case of the shablona module, the main classes defined at the bottom of the file make use of some of the functions defined in preceding lines.

## Project Data
In this case, the project data is rather small, and recorded in csv files. Thus, it can be stored alongside the module code. Even if the data that you are analyzing is too large, and cannot be effectively tracked with github, you might still want to store some data for testing purposes. 

Either way, you can create a `shablona/data` folder in which you can organize the data. Treating your data, and this folder, as 'read only' is a good idea. 

## Testing 

The idea behind software testing is that you want to make sure that your code does what you want it to do. Most scientists writing code are neither in a position to writ a complete [specification](http://www.wired.com/2013/01/code-bugs-programming-why-we-need-specs/), because when they start writing their code, they don't quite know what they will discover in their data, and that might affect where they go further. but it does at least specify certain inputs and output relationships that need to hold in your code. Better still, testing allows you to continuously monitor that the input-output relationships described in your tests still hold, as you continue to develop your software. More on that [below](## Continuous integration).

In practice, tests go into the `shablona/tests` folder. We recommend using the ['Nose'](http://nose.readthedocs.org/) library for testing. The `nosetests` application traverses the directory tree in which it is issued, looking for files with the names `test_*.py` (typically, something like our `shablona/tests/test_shablona.py`). Within each of these files, it looks for functions named `test_*`. Typically each function in the module would have a . This is sometimes called 'unit testing'. Other tests might check that a particular value is calculated to be the same value over time. This is sometimes called 'regression testing'. We have one such test in `shablona/tests/test_shablona.py` called `test_params_regression`.

## Documentation 

Documenting your software is a good idea. Not only as a way to communicate to others about how to use the software, but also as a way of reminding yourself what the issues are that you faced, and how you dealt with them, in a few months/years, when you return to looking at the code. 

To document `shablona` we use the [sphinx documentation system](http://sphinx-doc.org/). You can follw the instructions there on how to set up the system, but we have also already initialized and commited a skeleton documentation system in the `docs` directory.

Sphinx uses a Makefile to build different outputs of your documentation. For example, if you want to generate the HTML rendering of the documentation (web pages that you can upload to a website to explain the software).


## Installation

For installation and distribution we will use the python standard library `distutils` module. This module uses a `setup.py` file to figure out how to install your software on a particular system. For a small project such as this one, managing installation of the software modules and the data is rather simple. 

A `shablona/version.py` contains all of the information needed for the installation and for setting up the [PyPI page](https://pypi.python.org/pypi/shablona) for the software. This also makes it possible to install your software with using `pip` and `easy_install`, which are package managers for Python software. The `setup.py` file reads this information from there and passes it to the `setup` function which takes care of the rest. 

Much more information on packaging Python software can be found in the [Hitchhiker's guide to packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.org).


## Continuous integration

Travis-CI is a system that can be used to automatically test every revision of your code directly from github, including testing of github pull requests, before they are merged into the `master` branch. This provides you with information needed in order to evaluate contrubutions made by others. It also serves as a source of information for others interested in using or contributing to your project about the degree of test coverage of your project. 

You will need a .travis.yml file. This file contains the 

You will need to go to the Travis-CI [website]()


## Distribution
You will need to create a user account on PyPI.


[Instructions on deployment from PyPI with Travis](http://docs.travis-ci.com/user/deployment/pypi/).


## Licensing

License your code! A repository like this without a license is legally closed-source and cannot be used by others. Follow Jake's [advice](http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/)!

## Scripts 
A scripts directory can be used as a place to experiment with your module code, and as a place to produce scripts that contain a narrative structure, demonstrating the use of the code, or producing scientific results from your code and your data and telling a story with these elements.

For example, this repository contains an [IPython notebook] that reads. You can see this notebook fully rendered [here](https://github.com/uwescience/shablona/blob/master/scripts/Figure1.ipynb).