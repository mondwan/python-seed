python-seed
===========

Python seed project with requirements, tests, docs set up - opinions included

You can use this piecemeal or clone it to start new projects

---

Running Tests
-------------

You can run tests via the [nose library](https://pypi.python.org/pypi/nose).

Tests will be autodiscovered if they are in the `tests` folder, in files that start with `test_`.

To run the tests,

    nosetests -c .noserc

will run them based on the config settings in `.noserc`.

Two files will be placed in `test_results`:

* `nosetests.xml` - Logs what tests passed/failed, for CI software.
* `coverage.xml` - Logs the test coverage of your project, for CI software.

For more human-readable output, run

    nosetests -c .noserc_local

Then navigate to `test_results/coverage/index.html` and open it in your browser. This is the HTML interface for the
coverage report, and is very useful when writing tests to make sure your code is being executed.

`.coveragerc` contains the settings for the [coverage](https://pypi.python.org/pypi/coverage) library, and can be adjusted to filter analysis.

coverage will give errors when `nosetests` is run on an empty project - basically saying that there is no data.

Linting your Project
--------------------

Linting your project can improve your code quality and readability, as well as prevent some types of bugs and design anti-patterns.

Run [pylint](https://pypi.python.org/pypi/pylint) on your project with

	pylint -f parseable *.py tests --rcfile=.pylintrc | tee test_results/pylint.out
	
You can then check `test_results/pylint.out` for any violations.

Specific options for pylint are configured in `.pylintrc`.

You can also run [flake8](https://pypi.python.org/pypi/flake8) against your project with

	flake8 myapp
	
where myapp is any directory or Python module.

flake8 does 3 things: 

* Runs [pep8](https://pypi.python.org/pypi/pep8). pep8 is similar to pylint, some people prefer it.
* Runs [PyFlakes](https://pypi.python.org/pypi/pyflakes). This does some static analysis and detects potential errors.
* Optionally runs a McCabe complexity checker to report functions with complexity above a specified limit.

To enable the McCabe check, add this arg to your flake8 run

	--max-complexity 10
	
where 10 is the number you set.

Documenting your project
------------------------

Documentation is created via the [Sphinx](https://pypi.python.org/pypi/Sphinx) package. The docs live in the `docs` folder and use [RestructuredText](http://docutils.sourceforge.net/rst.html).

All doc files should use the `.rst` extension.

To generate html docs from your ReST source files

	cd docs
	make html
	
Then open `docs/_build/html/index.html` in your browser to view them.

`docs/conf.py` holds a number of settings for Sphinx, including theme, copyright and plugins.

Three plugins are already enabled:

* sphinx.ext.autodoc - By documenting your Python source code in ReST format, Sphinx can extract your docstrings into the docs.
* sphinx.ext.coverage - Gives you stats on how much of your code is documented.
* sphinx.ext.viewcode - Allows you to view your source code directly from the docs.

**ReST resources**

* [Primer](http://docutils.sourceforge.net/docs/user/rst/quickstart.html)
* [User Reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
* [Cheat Sheet](http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt)

3rd Party Packages
------------------

All packages that your project needs to run are listed in `requirements.txt`.

Any packages that are used only for development or build are listed in `requirements_dev.txt`.

You can install packages from both with

	pip install -r requirements.txt; pip install -r requirements_dev.txt