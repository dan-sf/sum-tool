import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'sum_tool', '__version__.py')) as fh:
    exec(fh.read(), about)

setup(
    name='sum-tool',
    description='Command line tool for summing numerical data',
    version = about['version'],
    packages=['sum_tool'],
    test_suite='tests',
    tests_require=[
        'mock',
    ],
    entry_points={ 'console_scripts': [ 'sum-tool = sum_tool.summation:main' ] }
)

