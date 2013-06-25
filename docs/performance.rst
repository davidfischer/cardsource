Performance
===========

There is a small performance suite which can be run with the following:

::

    % python setup.py performance


Raw data
--------

+---------------+----------+
|               | v0.0.1   |
+===============+==========+
| **Python2.6** | 20.77s   |
+---------------+----------+
| **Python2.7** | 21.13s   |
+---------------+----------+
| **Python3.3** | 27.32s   |
+---------------+----------+
| **Pypy**      | 1.333s   |
+---------------+----------+

The moral of the performance story is that Pypy should be used if performance
is important for your use case. However, the current performance tests
probably overstate Pypy's performance.