try:
    from setuptools import setup
except ImportError:
    from distutils import setup


long_description = open('README.rst').read()

setup(
    name = 'cardsource',
    version = '0.0.1',
    description = 'A Python library for simulating playing card games',
    long_description = long_description,
    author = 'David Fischer',
    author_email = 'djfische@gmail.com',
    url = 'https://github.com/davidfischer/cardsource',
    license = 'BSD',
    platforms = ['OS Independent'],
    packages = ['cardsource'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='tests',
)
