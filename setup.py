from setuptools import setup, find_packages
from distutils.core import Command


class PerformanceCommand(Command):
    description = 'Runs performance metrics'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import timeit
        performance = [
            {
                'desc': 'Aces count',
                'stmt': 'performance.aces_count()',
                'setup': 'import performance',
                'number': 1,
                'repeat': 10,
            }
        ]

        for perf in performance:
            timing = timeit.repeat(perf['stmt'],
                                   setup=perf['setup'],
                                   number=perf['number'],
                                   repeat=perf['repeat'])
            print('{0} took {1:.4}s'.format(perf['desc'], min(timing)))


long_description = open('README.rst').read()

setup(
    name='cardsource',
    version='0.0.1',
    description='A Python library for simulating playing card games',
    long_description=long_description,
    author='David Fischer',
    author_email='djfische@gmail.com',
    url='https://github.com/davidfischer/cardsource',
    license='BSD',
    platforms=['OS Independent'],
    packages=[p for p in find_packages('.') if p.startswith('cardsource')],
    classifiers=[
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
    cmdclass={
        'performance': PerformanceCommand
    }
)
