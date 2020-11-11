"""
Una regla representa el como cambia el estado de cada celula, esto es,
representa la vecindad y la funcion de transicion que se aplica a la
vecindad

En este modulo se implementan las reglas para la definicion de automatas
celulares bidimensionales
"""
import numpy as np

from pycellslib.twodimensional.neighborhoods import MooreNeighborhood
from pycellslib import Rule



class BSNotationRule(Rule):
    """
    Esta clase representa las reglas de transicion denotadas con la notacion
    B/S Notation
    """

    def __init__(self, B, S, radius=1):
        self.B = B
        self.S = S
        self.radius = radius
        self.neighborhood = MooreNeighborhood(radius=radius, inclusive=True)

    def get_neighborhood(self):
        """
        Este metodo retorna la vecindad asociada a la regla

        Returns
        -------
        out(Neighborhood): Objeto que representa la vecindad
        """
        return self.neighborhood

    def apply_rule(self, cell_states, cell_attributes=None):
        """
        Params
        ------
        cell_states(ndarray(int)):

        Returns
        -------
        out(int):
        """
        # indice de la celula del centro
        current_cell = cell_states[cell_states.size // 2]
        # para no contar a la celula del centro se establece el valor a cero
        cell_states[cell_states.size // 2] = 0

        alive_cells = np.sum(cell_states)

        new_state = 0
        if current_cell == 1:
            if self.S == []:
                new_state = 0
            if alive_cells in self.S:
                new_state = 1

        if current_cell == 0:
            if self.B == []:
                new_state = 1
            if alive_cells in self.B:
                new_state = 1

        return new_state, None
