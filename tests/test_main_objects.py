"""
En este script se testean objetos iniciales (que no dependen de
ninguna caracteristica particular de cualquier automata, como la dimensiona-
lidad, ...), esto es, en general aquellos cuya implementacion esta en
./pycellslib/__init__.py
"""

import unittest

from pycellslib import StandardCell


class TestStandardCell(unittest.TestCase):
    """
    Test para la clase StandardCell
    """


if __name__ == '__main__':
    unittest.main()
