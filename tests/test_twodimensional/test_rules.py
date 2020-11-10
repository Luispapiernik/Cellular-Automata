"""
En este script se testea las reglas implementadas para los casos
bidimensionales
"""

import unittest
import numpy as np

from pycellslib.twodimensional.neighborhoods import MooreNeighborhood
from pycellslib.twodimensional.rules import BSNotationRule


class TestBSNotationRule(unittest.TestCase):
    """
    Tests para la clase BSNotationRule
    """
