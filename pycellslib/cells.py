"""
Una celula es una entidad que puede tener n estados representados por
numeros enteros, y que tienen algun nombre, adicionalmente, la celula tiene
atributos asociados, que son tambien valores numericos con nombre, estos se
pueden usar para representar variables fisicas (velocidad, ...), variables
demograficas, ...

En este modulo se implementan las celulas mas comunes (celula del juego de la
vida, ...) usadas en automatas celulares
"""

from pycellslib import CellInformation


class StandardCell(CellInformation):
    """
    Esta clase
    """

    def __init__(self, start=None, end=None, step=None, default_state=None,
                 name_of_states=None):
        pass

    def get_states(self):
        """
        Este metodo retorna los posibles estados que puede tener una celula

        Returns
        -------
        out(list(int)): Posibles estados que puede tener una celula
        """

    def get_number_of_attributes(self):
        """
        Este metodo retorna el numero de atributos que tiene una celula. En
        caso de que la celula no tenga atributos se retorna 0

        Returns
        -------
        out(int): numero de atributos de una celula
        """

    def get_default_state(self):
        """
        Este metodo retorna el valor del estado que tienen las celulas por
        defecto

        Returns
        -------
        out(int): valor del estado por defecto de la celula
        """

    def get_default_value_of_attributes(self):
        """
        Este metodo retorna los valores que tiene una celula por defecto en
        cada atributo. En caso de que la celula no tenga atributos, se retorna
        None

        Returns
        -------
        out(None): valores por defecto de los atributos de la celula.
        """
    # con el objetivo de obtener y mostrar informacion del automata, como
    # densidad o flujo de celulas en un estado, ... se nombran los estados
    def get_name_of_state(self, state):
        """
        Este metodo retorna el nombre asociado a un estado.

        Params
        ------
        state(int): valor del estado del que se desea conocer el nombre

        Returns
        -------
        out(str): nombre del estado
        """

    # con el objetivo de obtener y mostrar informacion del automata, como
    # densidad, flujos, ... se nombran los atributos, los cuales tienen un
    # orden fijo
    def get_name_of_attribute(self, index):
        """
        Este metodo retorna el nombre del atributo asociado a un indice, el
        indice cuenta desde cero. Se retorna None en caso de que la celula no
        tenga atributos

        Params
        ------
        index(int): indice que corresponde al atributo

        Returns
        -------
        out(None): nombre del atributo, puede ser un string vacio
        """


class LifeLikeCell(StandardCell):
    pass
