## shablona
[![Build Status](https://travis-ci.org/uwescience/shablona.svg?branch=master)](https://travis-ci.org/uwescience/shablona)

Shablona is a template project for small scientific python projects. The
recommendations we make here follow the standards and conventions of much of
the scientific Python eco-system. Following these standards and recommendations
will make it easier for others to use your code, and can make it easier for you
to port your code into other projects and collaborate with other users of this
eco-system.

To use it as a template for your own project, click the green "use this template" 
button at the top of the front page of this repo.

First, let me explain all the different moving parts that make up a small
scientific python project, and all the elements which allow us to effectively
share it with others, test it, document it, and track its evolution.

### Organization of the  project

The project has the following structure:

    shablona/
      |- README.md
      |- shablona/
         |- __init__.py
         |- shablona.py
         |- due.py
         |- data/
            |- ...
         |- tests/
            |- ...
      |- doc/
         |- Makefile
         |- conf.py
         |- sphinxext/
            |- ...
         |- _static/
            |- ...
      |- setup.py
      |- .travis.yml
      |- .mailmap
      |- appveyor.yml
      |- LICENSE
      |- Makefile
      |- ipynb/
         |- ...


In the following sections we will examine these elements one by one. First,
let's consider the core of the project. This is the code inside of
`shablona/shablona.py`. The code provided in this file is intentionally rather
simple. It implements some simple curve-fitting to data from a psychophysical
experiment. It's not too important to know what it does, but if you are really
interested, you can read all about it
[here](http://arokem.github.io/2014-08-12-learn-optimization.html).

### Module code

We place the module code in a file called `shablona.py` in directory called
`shablona`. This structure is a bit confusing at first, but it is a simple way
to create a structure where when we type `import shablona as sb` in an
interactive Python session, the classes and functions defined inside of the
`shablona.py` file are available in the `sb` namespace. For this to work, we
need to also create a file in `__init__.py` which contains code that imports
everything in that file into the namespace of the project:

    from .shablona import *

In the module code, we follow the convention that all functions are either
imported from other places, or are defined in lines that precede the lines that
use that function. This helps readability of the code, because you know that if
you see some name, the definition of that name will appear earlier in the file,
either as a function/variable definition, or as an import from some other module
or package.

In the case of the shablona module, the main classes defined at the bottom of
the file make use of some of the functions defined in preceding lines.

Remember that code will be probably be read more times than it will be written.
Make it easy to read (for others, but also for yourself when you come back to
it), by following a consistent formatting style. We strongly recommend
following the
[PEP8 code formatting standard](https://www.python.org/dev/peps/pep-0008/), and
we enforce this by running a code-linter called
[`flake8`](http://flake8.pycqa.org/en/latest/), which automatically checks the
code and reports any violations of the PEP8 standard (and checks for other
  general code hygiene issues), see below.

### Project Data

In this case, the project data is rather small, and recorded in csv
files.  Thus, it can be stored alongside the module code.  Even if the
data that you are analyzing is too large, and cannot be effectively
tracked with github, you might still want to store some data for
testing purposes.

Either way, you can create a `shablona/data` folder in which you can
organize the data. As you can see in the test scripts, and in the
analysis scripts, this provides a standard file-system location for
the data at:

    import os.path as op
    import shablona as sb
    data_path = op.join(sb.__path__[0], 'data')


### Testing

Most scientists who write software constantly test their code. That is, if you
are a scientist writing software, I am sure that you have tried to see how well
your code works by running every new function you write, examining the inputs
and the outputs of the function, to see if the code runs properly (without
error), and to see whether the results make sense.

Automated code testing takes this informal practice, makes it formal, and
automates it, so that you can make sure that your code does what it is supposed
to do, even as you go about making changes around it.

Most scientists writing code are not really in a position to write a complete
[specification](http://www.wired.com/2013/01/code-bugs-programming-why-we-need-specs/)
of their software, because when they start writing their code they don't quite
know what they will discover in their data, and these chance discoveries might
affect how the software evolves. Nor do most scientists have the inclination to
write complete specs - scientific code often needs to be good enough to cover
our use-case, and not any possible use-case. Testing the code serves as a way to
provide a reader of the code with very rough specification, in the sense that it
at least specifies certain input/output relationships that will certainly hold
in your code.

We recommend using the ['pytest'](http://pytest.org/latest/) library for
testing. The `py.test` application traverses the directory tree in which it is
issued, looking for files with the names that match the pattern `test_*.py`
(typically, something like our `shablona/tests/test_shablona.py`). Within each
of these files, it looks for functions with names that match the pattern
`test_*`. Typically each function in the module would have a corresponding test
(e.g. `test_transform_data`). This is sometimes called 'unit testing', because
it independently tests each atomic unit in the software. Other tests might run a
more elaborate sequence of functions ('end-to-end testing' if you run through
the entire analysis), and check that particular values in the code evaluate to
the same values over time. This is sometimes called 'regression testing'. We
have one such test in `shablona/tests/test_shablona.py` called
`test_params_regression`. Regressions in the code are often canaries in the coal
mine, telling you that you need to examine changes in your software
dependencies, the platform on which you are running your software, etc.

Test functions should contain assertion statements that check certain relations
in the code. Most typically, they will test for equality between an explicit
calculation of some kind and a return of some function. For example, in the
`test_cumgauss` function, we test that our implmentation of the cumulative
Gaussian function evaluates at the mean minus 1 standard deviation to
approximately (1-0.68)/2, which is the theoretical value this calculation should
have. We recommend using functions from the `numpy.testing` module (which we
import as `npt`) to assert certain relations on arrays and floating point
numbers. This is because `npt` contains functions that are specialized for
handling `numpy` arrays, and they allow to specify the tolerance of the
comparison through the `decimal` key-word argument.

To run the tests on the command line, change your present working directory to
the top-level directory of the repository (e.g. `/Users/arokem/code/shablona`),
and type:

    py.test shablona

This will exercise all of the tests in your code directory. If a test fails, you
will see a message such as:


    shablona/tests/test_shablona.py .F...

    =================================== FAILURES ===================================
    ________________________________ test_cum_gauss ________________________________

      def test_cum_gauss():
          sigma = 1
          mu = 0
          x = np.linspace(-1, 1, 12)
          y = sb.cumgauss(x, mu, sigma)
          # A basic test that the input and output have the same shape:
          npt.assert_equal(y.shape, x.shape)
          # The function evaluated over items symmetrical about mu should be
          # symmetrical relative to 0 and 1:
          npt.assert_equal(y[0], 1 - y[-1])
          # Approximately 68% of the Gaussian distribution is in mu +/- sigma, so
          # the value of the cumulative Gaussian at mu - sigma should be
          # approximately equal to (1 - 0.68/2). Note the low precision!
    >       npt.assert_almost_equal(y[0], (1 - 0.68) / 2, decimal=3)
    E       AssertionError:
    E       Arrays are not almost equal to 3 decimals
    E        ACTUAL: 0.15865525393145707
    E        DESIRED: 0.15999999999999998

    shablona/tests/test_shablona.py:49: AssertionError
    ====================== 1 failed, 4 passed in 0.82 seconds ======================

This indicates to you that a test has failed. In this case, the calculation is
accurate up to 2 decimal places, but not beyond, so the `decimal` key-word
argument needs to be adjusted (or the calculation needs to be made more
accurate).

As your code grows and becomes more complicated, you might develop new features
that interact with your old features in all kinds of unexpected and surprising
ways. As you develop new features of your code, keep running the tests, to make
sure that you haven't broken the old features.  Keep writing new tests for your
new code, and recording these tests in your testing scripts. That way, you can
be confident that even as the software grows, it still keeps doing correctly at
least the few things that are codified in the tests.

We have also provided a `Makefile` that allows you to run the tests with more
verbose and informative output from the top-level directory, by issuing the
following from the command line:

    make test

### Styling

It is a good idea to follow the PEP8 standard for code formatting. Common code
formatting makes code more readable, and using tools such as `flake8` (which
combines the tools `pep8` and `pyflakes`) can help make your code more readable,
avoid extraneous imports and lines of code, and overall keep a clean project
code-base.

Some projects include `flake8` inside their automated tests, so that every pull
request is examined for code cleanliness.

In this project, we have run `flake8` most (but not all) files, on
most (but not all) checks:

```
flake8 --ignore N802,N806 `find . -name *.py | grep -v setup.py | grep -v /doc/`
```

This means, check all .py files, but exclude setup.py and everything in
directories named "doc". Do all checks except N802 and N806, which enforce
lowercase-only names for variables and functions.

The `Makefile` contains an instruction for running this command as well:

    make flake8

### Documentation

Documenting your software is a good idea. Not only as a way to communicate to
others about how to use the software, but also as a way of reminding yourself
what the issues are that you faced, and how you dealt with them, in a few
months/years, when you return to look at the code.

The first step in this direction is to document every function in your module
code. We recommend following the [numpy docstring
standard](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt),
which specifies in detail the inputs/outputs of every function, and specifies
how to document additional details, such as references to scientific articles,
notes about the mathematics behind the implementation, etc.

This standard also plays well with a system that allows you to create more
comprehensive documentation of your project. Writing such documentation allows
you to provide more elaborate explanations of the decisions you made when you
were developing the software, as well as provide some examples of usage,
explanations of the relevant scientific concepts, and references to the relevant
literature.

To document `shablona` we use the [sphinx documentation
system](http://sphinx-doc.org/). You can follow the instructions on the sphinx
website, and the example [here](http://matplotlib.org/sampledoc/) to set up the
system, but we have also already initialized and commited a skeleton
documentation system in the `docs` directory, that you can build upon.

Sphinx uses a `Makefile` to build different outputs of your documentation. For
example, if you want to generate the HTML rendering of the documentation (web
pages that you can upload to a website to explain the software), you will type:

	make html

This will generate a set of static webpages in the `doc/_build/html`, which you
can then upload to a website of your choice.

Alternatively, [readthedocs.org](https://readthedocs.org) (careful,
*not* readthedocs.**com**) is a service that will run sphinx for you,
and upload the documentation to their website. To use this service,
you will need to register with RTD. After you have done that, you will
need to "import your project" from your github account, through the
RTD web interface. To make things run smoothly, you also will need to
go to the "admin" panel of the project on RTD, and navigate into the
"advanced settings" so that you can tell it that your Python
configuration file is in `doc/conf.py`:

![RTD conf](https://github.com/uwescience/shablona/blob/master/doc/_static/RTD-advanced-conf.png)

 http://shablona.readthedocs.org/en/latest/


### Installation

For installation and distribution we will use the python standard
library `distutils` module. This module uses a `setup.py` file to
figure out how to install your software on a particular system. For a
small project such as this one, managing installation of the software
modules and the data is rather simple.

A `shablona/version.py` contains all of the information needed for the
installation and for setting up the [PyPI
page](https://pypi.python.org/pypi/shablona) for the software. This
also makes it possible to install your software with using `pip` and
`easy_install`, which are package managers for Python software. The
`setup.py` file reads this information from there and passes it to the
`setup` function which takes care of the rest.

Much more information on packaging Python software can be found in the
[Hitchhiker's guide to
packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.org).


### Continuous integration

Travis-CI is a system that can be used to automatically test every revision of
your code directly from github, including testing of github pull requests,
before they are merged into the `master` branch. This provides you with
information needed in order to evaluate contributions made by others. It also
serves as a source of information for others interested in using or contributing
to your project about the degree of test coverage of your project.

You will need a .travis.yml file in your repo. This file contains the
configuration of your testing environment. This includes the different
environments in which you will test the source code (for example, we test
`shablona` against Python 2.7, Python 3.3 and Python 3.4). It includes steps
that need to be taken before installation of the software. For example,
installation of the software dependencies. For `shablona`, we use the
[`Miniconda`](http://conda.pydata.org/miniconda.html) software distribution (not
to be confused with [`Anaconda`](https://store.continuum.io/cshop/anaconda/),
though they are similar and both produced by Continuum).

For details on setting up Travis-CI with github, see Travis-CI's
[getting started
page](https://docs.travis-ci.com/user/getting-started/#To-get-started-with-Travis-CI%3A). To
summarize:

First, go to the Travis-CI [website](https://travis-ci.org/) and get a
Travis user account, linked to your github user account.

You will need to set up your github repo to talk to Travis (More explanation +
pictures will come here).

You will need to go back to travis-ci, and flip on the switch on that side as
well.

The travis output will also report to you about test coverage, if you set it up
that way.

You will start getting emails telling you the state of the testing suite on
every pull request for the software, and also when you break the test suite on
the `master` branch. That way, you can be pretty sure that the `master` is
working (or at least know when it isn't...).

You can also continuously test your code on a Windows system. This is done on
another CI system called [Appveyor](http://www.appveyor.com/). In prinicple, it
does something that is very similar to what Travis does: downloads your code,
installs it on a Windows machine, with various versions of python, and runs the
tests. Appveyor is controlled through another configuration file: the
`appveyor.yml`. In addition to committing this file into the repository, you
will need to activate Appveyor for your project. This is done by signing into
the Appveyor interface with your Github account, clicking on the "projects" tab
at the top of the page, then clicking on the "+" sign for "New project" and
selecting the project you would like to add from the menu that appears (you
might need to give Appveyor the permission to see projects in your Github
account).

### Distribution

The main venue for distribution of Python software is the [Python
Package Index](https://pypi.python.org/), or PyPI, also lovingly known
as "the cheese-shop".

To distribute your software on PyPI, you will need to create a user account on
[PyPI](http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#register-your-project).
It is recommended that you upload your software using
[twine](http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#upload-your-distributions).

Using Travis, you can automatically upload your software to PyPI,
every time you push a tag of your software to github. The instructions
on setting this up can be found
[here](http://docs.travis-ci.com/user/deployment/pypi/). You will need
to install the travis command-line interface

### Licensing

License your code! A repository like this without a license maintains
copyright to the author, but does not provide others with any
conditions under which they can use the software. In this case, we use
the MIT license. You can read the conditions of the license in the
`LICENSE` file. As you can see, this is not an Apple software license
agreement (has anyone ever actually tried to read one of those?). It's
actually all quite simple, and boils down to "You can do whatever you
want with my software, but I take no responsibility for what you do
with my software"

For more details on what you need to think about when considering
choosing a license, see this
[article](http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/)!

### Getting cited

When others use your code in their research, they should probably cite you. To
make their life easier, we use [duecredit](http://www.duecredit.org). This is a software
library that allows you to annotate your code with the correct way to cite it.
To enable `duecredit`, we have added a file `due.py` into the main directory.
This file does not need to change at all (though you might want to occasionally
update it from duecredit itself. It's
[here](https://github.com/duecredit/duecredit/blob/master/duecredit/stub.py),
under the name `stub.py`).

In addition, you will want to provide a digital object identifier (DOI) to the
article you want people to cite.

To get a DOI, use the instructions in [this page](https://guides.github.com/activities/citable-code/)

Another way to get your software cited is by writing a paper. There are several
[journals that publish papers about software](https://www.software.ac.uk/resources/guides/which-journals-should-i-publish-my-software).

### Scripts

A scripts directory can be used as a place to experiment with your
module code, and as a place to produce scripts that contain a
narrative structure, demonstrating the use of the code, or producing
scientific results from your code and your data and telling a story
with these elements.

For example, this repository contains an [IPython notebook] that reads
in some data, and creates a figure. Maybe this is *Figure 1* from some
future article? You can see this notebook fully rendered
[here](https://github.com/uwescience/shablona/blob/master/scripts/Figure1.ipynb).


### Git Configuration

Currently there are two files in the repository which help working
with this repository, and which you could extend further:

- `.gitignore` -- specifies intentionally untracked files (such as
  compiled `*.pyc` files), which should not typically be committed to
  git (see `man gitignore`)
- `.mailmap` -- if any of the contributors used multiple names/email
  addresses or his git commit identity is just an alias, you could
  specify the ultimate name/email(s) for each contributor, so such
  commands as `git shortlog -sn` could take them into account (see
  `git shortlog --help`)


### Using `shablona` as a template

Let's assume that you want to create a small scientific Python project
called `smallish`. Maybe you already have some code that you are
interested in plugging into the module file, and some ideas about what
the tests might look like.

To use this repository as a template, click the green "use this template"
button on the front page of the "shablona" repository.

In "Repository name" enter the name of your project. For example, enter 
`smallish` here. After that, you can hit the "Create repository from template" 
button.

You should then be able to clone the new repo into your machine. You will want
to change the names of the files. For example, you will want to move
`shablona/shablona.py` to be called `smallish/smallish.py`

	git mv shablona smallish
	git mv smallish/shablona.py smallish/smallish.py
	git mv smallish/tests/test_shablona.py smallish/tests/test_smallish.py

Make a commit recording these changes. Something like:

	git commit -a -m"Moved names from `shablona` to `smallish`"

You will probably want to remove all the example data:

	git rm smallish/data/*
	git commit -a -m"Removed example `shablona` data"

Possibly, you will want to add some of your own data in there.

You will want to edit a few more places that still have `shablona` in them. Type
the following to see where all these files are:

	git grep shablona

You can replace `shablona` for `smallish` quickly with:

	git grep -l 'shablona' | xargs sed -i 's/shablona/smallish/g'

This very file (README.md) should be edited to reflect what your project is
about.

Other places that contain this name include the `doc/conf.py` file, which
configures the sphinx documentation, as well as the `doc/Makefile` file (edit
carefully!), and the `doc/index.rst` file.

The `.coveragerc` file contains a few mentions of that name, as well as the
`.travis.yml` file. This one will also have to be edited to reflect your PyPI
credentials (see [above](### Distribution)).

Edit all the mentions of `shablona` in the `shablona/__init__.py` file, and in
the `shablona/version.py` file as well.

Finally, you will probably want to change the copyright holder in the `LICENSE`
file to be you. You can also replace the text of that file, if it doesn't match
your needs.

At this point, make another commit, and continue to develop your own code based
on this template.
