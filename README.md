# shablona
[![Build Status](https://travis-ci.org/uwescience/shablona.svg?branch=master)](https://travis-ci.org/uwescience/shablona)

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

Most scientists who write software constantly test their code. That is, if you are a scientist writing software, I am sure that you have tried to see how well your code works by running every new function you write, examining the inputs and the outputs of the function, to see if the code runs properly (without error), and to see whether the results make sense. 

Automated code testing takes this informal practice, makes it formal, and automates it, so that you can make sure that your code does what it is supposed to do, even as you go about making changes around it. 

Most scientists writing code are not really in a position to write a complete [specification](http://www.wired.com/2013/01/code-bugs-programming-why-we-need-specs/) of their software, because when they start writing their code they don't quite know what they will discover in their data, and that might affect how the software evolves. Nor do most scientists have the inclination to write complete specs. Testing serves as a very rough specification, in the sense that it at least specifies certain input/output relationships that need to hold in your code. 

We recommend using the ['Nose'](http://nose.readthedocs.org/) library for testing. The `nosetests` application traverses the directory tree in which it is issued, looking for files with the names `test_*.py` (typically, something like our `shablona/tests/test_shablona.py`). Within each of these files, it looks for functions named `test_*`. Typically each function in the module would have a corresponding test (e.g. `test_transform_data`). This is sometimes called 'unit testing', becasue it independently tests each atomic unit in the software. Other tests might run a more elaborate sequence of functions ('end-to-end testing' if you run through the entire analysis), and check that particular values in the code evaluate to the same values over time. This is sometimes called 'regression testing'. We have one such test in `shablona/tests/test_shablona.py` called `test_params_regression`. Regressions in the code are often canaries in the coal mine, telling you that you need to examine changes in your software dependencies, the platform on which you are running your software, etc.

Test functions should contain assertion statements that check certain relations in the code. Most typically, they will test for equality between a calculation and a return of some function. We recommend using functions from the `numpy.testing` module (which we import as `npt`) to assert certain relations on arrays and floating point numbers. This is because `npt` contains functions that are specialized.

To run the tests on the command line, change your present working directory to the top-level directory of the repository (e.g. `/Users/arokem/code/shablona`), and type:

    nosetests

This will exercise all of the tests in your code directory. If a test fails, you will see a message 


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

You will need a .travis.yml file. This file contains the configuration of your testing environment. This includes the different environments in which you will test the source code (for example, we test `shablona` against Python 2.7, Python 3.3 and Python 3.4). It includes steps that need to be taken before installation of the software. For example, installation of the software dependencies. For `shablona`, we use the [`Miniconda`](http://conda.pydata.org/miniconda.html) software distribution (not to be confused with [`Anaconda`](https://store.continuum.io/cshop/anaconda/), though they are similar and both produced by Continuum).

You will need to go to the Travis-CI [website](https://travis-ci.org/). You will need to turn on the Travis service in your repo settings.

You will need to go to your account on Travis and flip on the switch that 


## Distribution

The main venue for distribution of Python software is the [Python Package Index](https://pypi.python.org/), or PyPI, also lovingly known as "the cheese-shop".  

To distribute your software on PyPI, you will need to create a user account on PyPI. You can upload your software using 


Using Travis, you can automatically upload your software to PyPI, every time you push a tag of your software to github. The instructions on setting this up can be found [here](http://docs.travis-ci.com/user/deployment/pypi/).

## Licensing

License your code! A repository like this without a license is legally closed-source and cannot be used by others. Follow Jake's [advice](http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/)!

## Scripts 
A scripts directory can be used as a place to experiment with your module code, and as a place to produce scripts that contain a narrative structure, demonstrating the use of the code, or producing scientific results from your code and your data and telling a story with these elements.

For example, this repository contains an [IPython notebook] that reads. You can see this notebook fully rendered [here](https://github.com/uwescience/shablona/blob/master/scripts/Figure1.ipynb).