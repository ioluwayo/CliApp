#!usr/bin/python
from setuptools import setup , find_packages
setup (
	name = 'CliApp',
	description = 'An application for converting numbers to words.',
	version = '0.10',
	packages = find_packages(), # list of all packages
    install_requires = ['inflect'],
    python_requires='>=2.7', # any python greater than 2.7
	test_suite="tests", # where to find tests
	entry_points = {
		'console_scripts': [
			'convert = convert.__main__:main', # got to module convert.__main__ and run the method called main
			'app2 = app2.__main__:main'
			]
		}
	)