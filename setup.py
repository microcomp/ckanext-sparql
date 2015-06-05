from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-sparql',
	version=version,
	description="Sparql_Point",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Jorge Pantoja',
	author_email='jorgepantojam@gmail.com',
	url='http://data.upf.edu',
	license='AGPL',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.sparql'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points={
        'babel.extractors': [
                'ckan = ckan.lib.extract:extract_ckan',
                ],
        'ckan.plugins' : [
                'sparql_interface = ckanext.sparql.plugin:SparqlPlugin',
                ],
        },
)
