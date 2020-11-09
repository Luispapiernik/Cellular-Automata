from setuptools import find_packages, setup

setup(name='pycellslib',
      version='0.0.1',
      description='Library for cellular automata simulation and visualization',
      url='https://github.com/computational-group-the-golden-ticket/Cellular-Automata',
      author='Luis Papiernik',
      author_email='lpapiernik24@gmail.com',
      license='GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007',

      packages=find_packages(exclude='__pycache__'),

      install_requires=['numpy'],

      zip_safe=False)
