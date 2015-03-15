python-seed
===========

Python seed project with requirements, tests, docs set up - opinions included

You can use this piecemeal or clone it to start new projects

---

Getting start
-------------

* Clone my repository

        git clone https://github.com/mondwan/python-seed.git
        cd python-seed

* Setup virtualenv (Optional)

        mkdir env
        virtualenv env/
        source env/bin/activate

* Install dependencies

        pip install -r requirements.txt

* Update setup.cfg with information like author, name of project etc

* Code your application

    * Remember to rename directory ***YOUR_PROJECT_NAME***

Running Tests
-------------

You can run tests via the [nose library](https://pypi.python.org/pypi/nose).

Tests will be autodiscovered if they are in the `tests` folder, in files that
start with `test_`.

To run the tests,

    nosetests -c .noserc

will run them based on the config settings in `.noserc`.

Two files will be placed in `test_results`:

* `nosetests.xml` - Logs what tests passed/failed, for CI software.
* `coverage.xml` - Logs the test coverage of your project, for CI software.

For more human-readable output, run

    nosetests -c .noserc_local

Then navigate to `test_results/coverage/index.html` and open it in your
browser. This is the HTML interface for the coverage report, and is very useful
when writing tests to make sure your code is being executed.

`.coveragerc` contains the settings for the [coverage][coverage] library, and
can be adjusted to filter analysis.

coverage will give errors when `nosetests` is run on an empty project which is
basically saying that there is no data.

[coverage]: https://pypi.python.org/pypi/coverage

Documentation
-------------

Documentation is created via the [Sphinx][Sphinx] package. The docs live in
the `docs` folder and use [RestructuredText][RestructuredText].

All doc files should use the `.rst` extension.

[Sphinx]: https://pypi.python.org/pypi/Sphinx
[RestructuredText]: http://docutils.sourceforge.net/rst.html

Getting start
=============

* Initialize documentation directory

        # Get in documentation directory
	    cd docs
	    # Generate 2 files
	    fab initialize

	    # After running initialize, you should get 2 files `docs/src/index.rst` and
	    # `docs/build/conf.py`

* Write your own .rst files and placed under folder `docs/src`

* Generate html

        fab make
	
* open `docs/build/html/index.html` in your browser to view them.

Notes
=====

Three plugins are already enabled:

* `sphinx.ext.autodoc` - By documenting your Python source code in ReST format,
  Sphinx can extract your docstrings into the docs.

* `sphinx.ext.coverage` - Gives you stats on how much of your code is documented.

* `sphinx.ext.viewcode` - Allows you to view your source code directly from the docs.

ReST resources
==============

* [Primer](http://docutils.sourceforge.net/docs/user/rst/quickstart.html)
* [User Reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
* [Cheat Sheet](http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt)

Distribution
------------

You should take care below 2 files before distributing your application.

    # setup.py
    # requirement.txt

* setup.py

Make sure you have written all your python modules into the attribute
```package```

* requirement.txt

Make sure you have written all dependencies you need there
