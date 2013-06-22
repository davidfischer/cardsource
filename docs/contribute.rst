Contributing
============

Cardsource should work and is tested on Python 2.6+, 3.3+ and pypy. Pull
requests are welcomed on GitHub_, but major changes should probably be
discussed before simply sending a huge patch.

.. _GitHub: https://github.com/davidfischer/cardsource


Semantic versioning
-------------------

Cardsource uses `semantic versioning`_ which means that it declares a public
API and acts reasonably with respect to version numbers. However, since
cardsource has a major version of zero (0.y.x) the public API should not be
considered entirely stable. Backward incompatible changes are not introduced
lightly and will be documented in depth in the changelog.

.. _semantic versioning: http://semver.org/


Unit testing
------------

All patches that add features or fix bugs should come with unit tests.
Unit tests are run automatically as part of continuous integration and
can be run manually with:

::

    % python setup.py test

If tox_ is installed, unit tests for all supported Python versions can be
run with the following command. See ``.tox.ini`` for details.

::

    % tox

.. _tox: http://tox.readthedocs.org/


Code quality
------------

All code under pokersource is run through flake8_ as part of continuous
integration. See ``.travis.yml`` for details.

.. _flake8: https://pypi.python.org/pypi/flake8


Documentation
-------------

This documentation is generated using the sphinx_ package. All patches
that change or add features should include associated documentation changes.

Generating the documentation is done with:

::

    % cd docs && make html

.. _sphinx: http://sphinx-doc.org/