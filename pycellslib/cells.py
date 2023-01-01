"""
Una celula es una entidad que puede tener n estados representados por
numeros enteros, y que tienen algun nombre, adicionalmente, la celula tiene
atributos asociados, que son tambien valores numericos con nombre, estos se
pueden usar para representar variables fisicas (velocidad, ...), variables
demograficas, ...

En este modulo se implementan las celulas mas comunes (celula del juego de la
vida, ...) usadas en automatas celulares
"""

from typing import Iterable, List, Optional, Union

import numpy as np
import numpy.typing as npt

from pycellslib.core import CellInformation


class StandardCell(CellInformation):
    """
    Esta clase representa una celula estandar, esto es, aquellas que no tienen
    atributos.

    Parameters
    ----------
    start: int | List[int] | Tuple[int] | npt.NDArray[int]
        Parametro usado para especificar los posibles estados del automata,
        cuando se pasa un iterable. Pero start toma un valor entero, se usa para
        especificar el rango en el que estan los estados.
    end: Optional[int]
        cuando el parametro start es un entero, este parametro es usado para
        especificar el rango en el que estan los estados
    step: Optional[int]
        el parametro start es un entero, este parametro es usado para
        especificar que enteros en el rango especificado hacen parte de los
        posibles estados
    default_state: Optional[int]
        valor por defecto que se usa para los estados
    states_names: Optional[Union[List[str], Tuple[str]]]
        nombre de cada estado
    """

    def __init__(
        self,
        start: Union[int, Iterable[int], npt.NDArray[np.int]],
        end: Optional[int] = None,
        step: Optional[int] = None,
        default_state: Optional[int] = None,
        states_names: Iterable[str] = [],
        attributes: Iterable[float] = [],
        attributes_names: Iterable[str] = [],
    ) -> None:
        self.states = (
            list(range(start if end else 0, end or start, step or 1))
            if isinstance(start, int)
            else list(start)
        )

        self.default_state = default_state or self.states[0]
        self.states_names = {
            key: value for key, value in zip(self.states, states_names)
        }

        self.default_attributes = list(attributes)
        self.attributes_names = {
            key: value for key, value in enumerate(attributes_names)
        }

    def get_states(self) -> List[int]:
        """
        Este metodo retorna los posibles estados que puede tener una celula

        Returns
        -------
        out: List[int]
            Posibles estados que puede tener una celula
        """
        return self.states[:]

    def get_states_number(self) -> int:
        return len(self.states)

    def get_attributes_number(self) -> int:
        """
        Este metodo retorna el numero de atributos que tiene una celula. En
        caso de que la celula no tenga atributos se retorna 0

        Returns
        -------
        out: int
            numero de atributos de una celula
        """
        return len(self.default_attributes)

    def get_default_state(self) -> int:
        """
        Este metodo retorna el valor del estado que tienen las celulas por
        defecto

        Returns
        -------
        out(int): valor del estado por defecto de la celula
        """
        return self.default_state

    def get_default_value_of_attributes(self):
        """
        Este metodo retorna los valores que tiene una celula por defecto en
        cada atributo. En caso de que la celula no tenga atributos, se retorna
        None

        Returns
        -------
        out(None): valores por defecto de los atributos de la celula.
        """
        return self.default_attributes[:]

    # con el objetivo de obtener y mostrar informacion del automata, como
    # densidad o flujo de celulas en un estado, ... se nombran los estados
    def get_state_name(self, state: int) -> str:
        """
        Este metodo retorna el nombre asociado a un estado.

        Parameters
        ----------
        state(int): valor del estado del que se desea conocer el nombre

        Returns
        -------
        out(str): nombre del estado
        """
        return self.states_names.get(state, "")

    # con el objetivo de obtener y mostrar informacion del automata, como
    # densidad, flujos, ... se nombran los atributos, los cuales tienen un
    # orden fijo
    def get_attribute_name(self, index: int):
        """
        Este metodo retorna el nombre del atributo asociado a un indice, el
        indice cuenta desde cero. Se retorna None en caso de que la celula no
        tenga atributos

        Parameters
        ----------
        index(int): indice que corresponde al atributo

        Returns
        -------
        out(None): nombre del atributo, puede ser un string vacio
        """
        return self.attributes_names.get(index, "")


class LifeLikeCell(StandardCell):
    """
    Esta clase representa a las celulas que se usan en el juego de la vida
    """

    def __init__(self) -> None:
        super().__init__([0, 1], states_names=["Dead", "Alive"])
