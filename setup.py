#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from distutils.core import setup
from setuptools import find_packages, Command

# Package meta-data
NAME = 'pymicrodose'
DESCRIPTION = 'Microdosimetric models by A. Bertolet'
URL = 'https://github.com/alebertolet/pymicrodose'
EMAIL = 'abertoletreina@mgh.harvard.edu'
AUTHOR = 'Alejandro Bertolet'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '1.1.2'

# Required packages for this module to be executed
REQUIRED = ['numpy', 'pandas', 'scipy']

# Optional packages
EXTRAS = { 'plots':['matplotlib'] }

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except:
    long_description = DESCRIPTION
    
# Load the package's __version__.py module as a dictionary
about = {}
if not VERSION:
    project_slug = "pyMicroDose"
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION
    
# Support setup.py upload
class UploadCommand(Command):
    description = 'Build and publish the package'
    user_options = []
    
    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))
        
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass
        
        self.status('Building source and wheel distribution...')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
        
        self.status('Uploading the package to PyPI via Twine...')
        os.system('twine upload dist/*')
        
        self.status('Pushing git tags...')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')
        
# Executing setup
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['pyMicroDose'],
    package_dir={'pyMicroDose': 'src'},
    package_data={'pyMicroDose': ['nist/*.csv']},
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    #include_package_data=True,
    zip_safe=False,
    license='MIT',
    classifiers=[
        'License :: MIT',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPhyton',
        'Programming Language :: Python :: Implementation :: PyPy'
        ],
    cmdclass={
        'upload' : UploadCommand,
        }
    )
            
