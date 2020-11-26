"""
Script usado para la configuracion e instalacion del paquete
"""

from setuptools import find_packages, setup

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(name='pycellslib',
      version='0.0.1',
      maintainer='Developers of the Computational Group The Golden Ticket',
      maintainer_email='cgthegoldenticket@gmail.com',
      description='Librería para la simulación y visualización de autómatas celulares.',
      long_description=long_description,
      url='https://github.com/computational-group-the-golden-ticket/Cellular-Automata',
      author='Luis Papiernik',
      author_email='lpapiernik24@gmail.com',
      license='GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007',
      classifiers=[
        'Development Status :: 5 - Beta/Testing',
        'Framework :: PyCellsLib',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development'
      ],
      test_suite='unittest',
      packages=find_packages(exclude='__pycache__'),
      keywords=['Automata celular', 'Sistemas complejos', 'Computacion', 'Dinamica no lineal'],
      python_requires='>=3.6',
      install_requires=['numpy', 'matplotlib', 'pygame'],
      zip_safe=False)
