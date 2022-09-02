from abc import ABCMeta, abstractmethod
from typing import Iterable, List, Optional, Tuple, Union

import numpy as np
import numpy.typing as npt

from pycellslib.utils import PositionIterator


class Topology(metaclass=ABCMeta):
    """
    La topologia representa la informacion espacial de una automata, esto es,
    tiene encapsulada las dimensiones, la distribucion de las celulas, los
    valores de estados y atributos en cada parte del espacio, metodos
    que extraen y asignan valores a subregiones del espacio...

    Internamente la clase Topology debe manejar 2 estructuras de datos para
    poder implementar la logica de actualizacion de las celulas (porque esta
    actualizacion se debe realizar en paralelo, es decir, en una de las
    estructuras de datos se van leyendo los valores, para poder calcular cual
    sera el nuevo valor en la siguiente iteracion, y en la otra estructura
    de datos se va escribiendo el nuevo valor de las celulas), por tanto en
    cada una de las estructuras se podra solo realizar una de dos, o escribir
    o leer (este comportamiento se puede modificar con el metodo flip, que
    invierte los papeles de lectura-escritura en las estructuras de datos).
    Ademas estas estructuras deben tener el cuenta el como la clase maneja
    las fronteras (las celulas de la frontera son no actualizables, su unico
    objetivo es el de hacer que todas las celulas actualizables tengan la
    misma condicion para las vecindades)
    """

    @abstractmethod
    def get_offset(self):
        """
        Este metodo debe retornar el offset que se le hacen a las posiciones
        en la matrix para no considerar las celulas de las fronteras en el
        proceso de actualizacion
        """

    @abstractmethod
    def __iter__(self):
        """
        La clase Topology debe brindar una interfaz por la cual se pueda
        iterar por cada celula para realizar el proceso de actualizacion, este
        metodo retorna un iterador sobre las posiciones de las celulas que son
        actualizables (esto es, las que no estan en la frontera)

        Returns
        -------
        out(iter(int)): iterador que recorre cada uno de los indices de las
            celulas que son actualizables
        """

    @abstractmethod
    def flip(self):
        """
        Este metodo cambia el papel (ser de lectura o ser de escritura) que
        cumplen las 2 estructuras de datos en las que se almacenan la
        informacion de estados y atributos de las celulas
        """

    @abstractmethod
    def get_cell(self, position):
        """
        Este metodo obtiene la informacion de una celula, tanto los estados
        como los atributos. Este metodo no permite obtener una celula que esta
        en la frontera

        Parameters
        ----------
        position(tuple(int)|list(int)|ndarray(int)): representan la posicion de
            la celula

        Returns
        -------
        outs(tuple): tupla cuya primera componente es un entero con el valor
            del estado de la celula asociada a la posicion dada, y la segunda
            componente es un array con el valor de los atributos, o None, en
            caso de que las celulas no tenga atributos
        """

    @abstractmethod
    def get_states(self):
        """
        Este metodo retorna los estados de las celulas, no se tiene en cuenta
        la frontera

        Returns
        -------
        out(list(int)|tuple(int)|ndarray(int)): estados de las celulas
        """

    @abstractmethod
    def get_attributes(self):
        """
        Este metodo retorna los atributos de las celulas, no se tiene en cuenta
        la frontera

        Returns
        -------
        out(list(float)|tuple(float)|ndarray(float)): atributos de las celulas
        """

    @abstractmethod
    def update_cell(self, position, cell_state, cell_attributes):
        """
        Este metodo actualiza la informacion de una celula, tanto estados como
        atributos

        Parameters
        ----------
        position(tuple|list): representa la posicion de la celula que sera
            actualizada
        cell_state(int): entero con el valor del estado de la celula
        cell_attributes(list(float)|ndarray(float)|None): lista o arreglo con
            los valores de los atributos. Si las celulas no tienen atributos
            se pasa None
        """

    @abstractmethod
    def set_border_values(self, cell_state, cell_attributes):
        """
        Este metodo establece el valor en los bordes

        Parameters
        ----------
        state_value(int): especifica el valor de los estados en los bordes
        attributes_values(list): especifica el valor de los atributos en los
            bordes, cada elemento de la lista especifica un atributo
        """

    @abstractmethod
    def set_values_from(self, cell_state, cell_attributes):
        """
        Este metodo establece el valor de las celulas usando los mismos
        parametros tanto para los estados, como para los atributos

        Parameters
        ----------
        cell_state(int): entero con el valor de los estados de las celulas
        cell_attributes(list|None): lista o arreglo con los valores de
            los atributos. Si las celulas no tienen atributos se pasa None
        """

    @abstractmethod
    def set_values_from_configuration(self, cell_states, cell_attributes):
        """
        Este metodo establece el valor de las celulas desde un arreglo de
        estados y un arreglo de atributos

        Parameters
        ----------
        cell_states(ndarray(int)): arreglo con los valores de los estados de
            cada celula
        cell_attributes(ndarray(float)|None): arreglo con los valores de los
            atributos de cada celula. Si las celulas no tienen atributos se
            pasa None
        """

    @abstractmethod
    def apply_mask(self, position, mask):
        """
        Este metodo retorna la vecindad de una celula mediante la aplicacion
        de la mascara que representa la vecindad

        Parameters
        ----------
        position(tuple(int)|list(int)): posicion en la que se ubica la mascara
        mask(ndarray): arreglo que representa alguna vecindad

        Returns
        ------
        out(tuple): Tupla donde la primera componente son los estados de las
            celulas que representan la vecindad, y la segunda componente
            representa los atributos de cada celula, si las celulas no tienen
            atributos se retorna None
        """


class FiniteNGridTopology(Topology):
    """
    La topologia representa la informacion espacial de una automata, esto es,
    tiene encapsulada las dimensiones, la distribucion de las celulas, los
    valores de estados y atributos en cada parte del espacio, metodos
    que extraen y asignan valores a subregiones del espacio...

    Esta clase representa una topologia rectangular n-dimensional finita, esto
    es, para 2 dimensiones se puede visualizar como una teselacion de
    rectangulos, para 3 dimensiones como una teselacion de cubos, ...

    Parameters
    ----------
    attributes_number(int): numero de atributos de cada celula en el espacio
    dimensions(tuple(int)|list(int)|ndarray(int)): dimensiones del espacio
    border_widths(tuple(int)|list(int)|ndarray(int)): dimensiones de la
        frontera. Estas dimensiones se le suman a las dimensiones del espacio
    """

    def __init__(
        self,
        attributes_number: int,
        dimensions: Union[Iterable[int], npt.NDArray[np.int]],
        border_widths: Union[Iterable[int], npt.NDArray[np.int]],
    ) -> None:
        # numero de atributos de cada celula en el espacio
        self.attributes_number = attributes_number
        # dimensiones del espacio sin tener en cuenta la frontera
        self.dimensions = np.array(dimensions, dtype=int)
        # dimensiones de la frontera
        self.border_widths = np.array(border_widths, dtype=int)

        # dimensiones reales del espacio, esto es, considerando la frontera
        self.real_dimensions = self.dimensions + 2 * self.border_widths

        # subregion del espacio completo, sin considerar la frontera
        self.subshape = tuple(
            slice(self.border_widths[i], self.dimensions[i] + self.border_widths[i])
            for i in range(self.dimensions.size)
        )

        # el indice 0 corresponde al buffer 1 y el indice 1 corresponde al
        # buffer 2
        self.states = [
            np.zeros(self.real_dimensions, dtype=int),
            np.zeros(self.real_dimensions, dtype=int),
        ]

        # si se tienen 0 atributos, entonces no hace falta crear un array
        self.attributes = []
        if attributes_number != 0:
            self.attributes = [
                np.zeros((*self.real_dimensions, attributes_number), dtype=float),
                np.zeros((*self.real_dimensions, attributes_number), dtype=float),
            ]

        # estos atributos llevan la cuenta de que buffer se usa para lectura y
        # que buffer se usa para escritura
        self.write_buffer = 0
        self.read_buffer = 1

    def get_offset(self) -> npt.NDArray[np.int]:
        """
        Este metodo debe retornar el offset que se le hacen a las posiciones
        en la matrix para no considerar las celulas de las fronteras en el
        proceso de actualizacion
        """
        return self.border_widths

    def __iter__(self) -> PositionIterator:
        """
        La clase Topology debe brindar una interfaz por la cual se pueda
        iterar por cada celula para realizar el proceso de actualizacion, este
        metodo retorna un iterador sobre las posiciones de las celulas que son
        actualizables (esto es, las que no estan en la frontera)

        Returns
        -------
        out(iter(list(tuple(int)))): iterador que recorre cada uno de los
            indices de las celulas que son actualizables
        """
        return PositionIterator(self.dimensions, self.border_widths)

    def flip(self) -> None:
        """
        Este metodo cambia el papel (ser de lectura o ser de escritura) que
        cumplen las 2 estructuras de datos en las que se almacenan la
        informacion de estados y atributos de las celulas
        """
        self.write_buffer += 1
        self.read_buffer += 1

        self.write_buffer %= 2
        self.read_buffer %= 2

    def get_cell(
        self, position: Tuple[int]
    ) -> Tuple[int, Optional[npt.NDArray[np.float]]]:
        """
        Este metodo obtiene la informacion de una celula, tanto los estados
        como los atributos. Este metodo no permite obtener una celula que esta
        en la frontera

        Parameters
        ----------
        position(tuple(int)): representan la posicion de la celula

        Returns
        -------
        outs(tuple): tupla cuya primera componente es un entero con el valor
            del estado de la celula asociada a la posicion dada, y la segunda
            componente es un array con el valor de los atributos, o None, en
            caso de que las celulas no tenga atributos
        """
        state = self.states[self.read_buffer][position]

        attributes = None
        if self.attributes is not None:
            attributes = self.attributes[self.read_buffer][position]

        return state, attributes

    def get_states(self) -> npt.NDArray[np.int]:
        """
        Este metodo retorna los estados de las celulas, no se tiene en cuenta
        la frontera

        Returns
        -------
        out(ndarray(int)): estados de las celulas
        """
        return self.states[self.read_buffer][self.subshape]

    def get_attributes(self) -> npt.NDArray[np.float]:
        """
        Este metodo retorna los atributos de las celulas, no se tiene en cuenta
        la frontera

        Returns
        -------
        out(ndarray(float)): atributos de las celulas
        """
        return self.attributes[self.read_buffer][self.subshape]

    def update_cell(
        self,
        position: Tuple[int, int],
        cell_state: int,
        cell_attributes: Optional[Union[List[float], npt.NDArray[np.float]]],
    ) -> None:
        """
        Este metodo actualiza la informacion de una celula, tanto estados como
        atributos

        Parameters
        ----------
        position(tuple(int)): representa la posicion de la celula que sera
            actualizada
        cell_state(int): entero con el valor del estado de la celula
        cell_attributes(list(float)|ndarray(float)|None): lista o arreglo con
            los valores de los atributos. Si las celulas no tienen atributos
            se pasa None
        """
        self.states[self.write_buffer][position] = cell_state

        if self.attributes is not None:
            self.attributes[self.write_buffer][position] = cell_attributes

    def set_border_values(
        self,
        cell_state: int,
        cell_attributes: Optional[Union[List[float], npt.NDArray[np.float]]] = None,
    ) -> None:
        """
        Este metodo establece el valor en los bordes

        Parameters
        ----------
        cell_state(int): especifica el valor de los estados en los bordes
        cell_attributes(list(float)|ndarray(float)|None): especifica el valor
            de los atributos en los bordes, cada elemento de la lista
            especifica un atributo
        """
        # se crea mascara para establecer el valor en los bordes
        mask = np.ones(self.real_dimensions, dtype=bool)
        # el subshape no hace parte de la frontera
        mask[self.subshape] = 0
        self.states[self.write_buffer][mask] = cell_state

        if self.attributes is not None:
            self.attributes[self.write_buffer][mask] = cell_attributes

    def set_values_from(
        self,
        cell_state: int,
        cell_attributes: Optional[Union[List[float], npt.NDArray[np.float]]] = None,
    ) -> None:
        """
        Este metodo establece el valor de las celulas usando los mismos
        parametros tanto para los estados, como para los atributos

        Parameters
        ----------
        cell_state(int): entero con el valor de los estados de las celulas
        cell_attributes(list(float)|ndarray(float)|None): especifica el valor
            de los atributos, si la celula no tiene atributos se pasa None
        """
        self.states[self.write_buffer][self.subshape] = cell_state

        if self.attributes is not None:
            self.attributes[self.write_buffer][self.subshape] = cell_attributes

    def set_values_from_configuration(
        self,
        cell_states: npt.NDArray[np.int],
        cell_attributes: Optional[npt.NDArray[np.float]] = None,
    ) -> None:
        """
        Este metodo establece el valor de las celulas desde un arreglo de
        estados y un arreglo de atributos

        Parameters
        ----------
        cell_states(ndarray(int)): arreglo con los valores de los estados de
            cada celula
        cell_attributes(ndarray(float)|None): arreglo con los valores de los
            atributos de cada celula. Si las celulas no tienen atributos se
            pasa None
        """
        self.states[self.write_buffer][self.subshape] = cell_states

        if self.attributes is not None:
            self.attributes[self.write_buffer][self.subshape] = cell_attributes

    def apply_mask(
        self, position: Tuple[int, int], mask: npt.NDArray[np.int]
    ) -> Tuple[npt.NDArray[np.int], npt.NDArray[np.float]]:
        """
        Este metodo retorna la vecindad de una celula mediante la aplicacion
        de la mascara que representa la vecindad

        Parameters
        ----------
        position(tuple(int)): posicion en la que se ubica la mascara, esta
            posicion debe tener en cuenta la frontera y las dimensiones de la
            mascara
        mask(ndarray): arreglo que representa alguna vecindad

        Returns
        ------
        out(tuple): Tupla donde la primera componente es un array con los
            estados de las celulas que representan la vecindad, y la segunda
            componente un array con los atributos de cada celula, si las
            celulas no tienen atributos se retorna None
        """
        # se extrae la region en donde se aplicara la mascara
        subshape = tuple(
            slice(position[i], position[i] + mask.shape[i])
            for i in range(len(mask.shape))
        )

        states = self.states[self.read_buffer][subshape][mask]

        attributes = None
        if self.attributes is not None:
            attributes = self.attributes[self.read_buffer][subshape][mask]

        return states, attributes
