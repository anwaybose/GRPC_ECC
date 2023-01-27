'''
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
    packages=['python_crypto'],
    package_dir={'': 'src'}
)
setup(**d)
'''

#!/usr/bin/env python

from distutils.core import setup

setup(
      version='1.0',
      description='Pycryptodome',
      author='Anway Bose',
      author_email='anway.bose@gmail.com',
      url='https://github.com/anwaybose/Crypto',
      packages=['python_crypto'],
      package_dir={'': 'src'}
     )