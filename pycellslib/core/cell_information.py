from abc import ABCMeta, abstractmethod
from optparse import Option
from typing import Iterable, List, Optional, Tuple, Union

import numpy as np
import numpy.typing as npt


class CellInformation(metaclass=ABCMeta):
    """
    Una celula es una entidad que puede tener n estados representados por
    numeros enteros, y que tienen algun nombre, adicionalmente, la celula tiene
    atributos asociados, que son tambien valores numericos con nombre, estos se
    pueden usar para representar variables fisicas (velocidad, ...), variables
    demograficas, ...

    Esta es la clase base de las que deben heredar aquellas clases que brindan
    informacion de los parametros asociados a las celulas de algun automata.
    """

    @abstractmethod
    def get_states(self):
        """
        Este metodo retorna una tupla, lista o arreglo de los posibles estados
        que puede tener una celula

        Returns
        -------
        out(tuple(int)|list(int)|ndarray(int)): Posibles estados que puede
            tener una celula
        """

    @abstractmethod
    def get_number_of_attributes(self):
        """
        Este metodo retorna el numero de atributos que tiene una celula. En
        caso de que la celula no tenga atributos se retorna 0

        Returns
        -------
        out(int): numero de atributos de una celula
        """

    @abstractmethod
    def get_default_state(self):
        """
        Este metodo retorna el valor del estado que tienen las celulas por
        defecto

        Returns
        -------
        out(int): valor del estado por defecto de la celula
        """

    @abstractmethod
    def get_default_value_of_attributes(self):
        """
        Este metodo retorna los valores que tiene una celula por defecto en
        cada atributo. En caso de que la celula no tenga atributos, se retorna
        None

        Returns
        -------
        out(list|ndarray|None): valores por defecto de los atributos de la
            celula.
        """

    # con el objetivo de obtener y mostrar informacion del automata, como
    # densidad o flujo de celulas en un estado, ... se nombran los estados
    @abstractmethod
    def get_name_of_state(self, state):
        """
        Este metodo retorna el nombre asociado a un estado.

        Parameters
        ----------
        state(int): valor del estado del que se desea conocer el nombre

        Returns
        -------
        out(str): nombre del estado, puede ser un string vacio
        """

    # con el objetivo de obtener y mostrar informacion del automata, como
    # densidad, flujos, ... se nombran los atributos, los cuales tienen un
    # orden fijo
    @abstractmethod
    def get_name_of_attributes(self, index):
        """
        Este metodo retorna el nombre del atributo asociado a un indice, el
        indice cuenta desde cero. Se retorna None en caso de que la celula no
        tenga atributos

        Parameters
        ----------
        index(int): indice que corresponde al atributo

        Returns
        -------
        out(str|None): nombre del atributo, puede ser un string vacio
        """
