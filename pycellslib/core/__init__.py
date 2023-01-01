"""
Este modulo tendra la implementacion de objetos iniciales (que no dependen de
ninguna caracteristica particular de cualquier automata, como la dimensiona-
lidad, ...) tanto abstractos como no abstractos, estos son, aquellos que
codifican la informacion y comportamiento de las celulas (CellularInformation),
de la topologia (Topology, ...), de la vecindad (Neighborhood), la informacion
de las funciones de transicion y de como se relacionan todos estos objetos
entre si (con el objeto Automata)
"""

from pycellslib.core.automaton import Automaton
from pycellslib.core.cell_information import CellInformation
from pycellslib.core.neighborhood import Neighborhood
from pycellslib.core.position_iterator import NGridIterator
from pycellslib.core.rule import Rule
from pycellslib.core.topology import FiniteNGridTopology, Topology

__all__ = [
    "Automaton",
    "CellInformation",
    "Rule",
    "Topology",
    "FiniteNGridTopology",
    "Neighborhood",
    "NGridIterator",
]
