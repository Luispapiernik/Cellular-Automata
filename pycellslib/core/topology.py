from abc import ABCMeta, abstractmethod
from typing import Iterable, List, Optional, Tuple, Type, Union

import numpy as np
import numpy.typing as npt

from pycellslib.core.position_iterator import NGridIterator


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

    # @abstractmethod
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


class FiniteNGridTopology:
    def __init__(
        self,
        attributes_number: int,
        dimensions: Union[Iterable[int], npt.NDArray[np.int]],
        frontiers_width: Union[Iterable[int], npt.NDArray[np.int]],
        memory_length: int,
    ) -> None:
        self.dimensions = np.array(dimensions, dtype=int)
        self.frontiers_width = np.array(frontiers_width, dtype=int)
        self.sub_dimensions = self.dimensions - 2 * self.frontiers_width

        # The +1 in the second component stands for states, that is, index
        # 0 is for states
        self.cells = np.zeros(
            (
                memory_length,
                attributes_number + 1,  # to save states along with attributes
                *self.dimensions,
            )
        )

        # Region without frontiers
        not_frotier = tuple(
            slice(self.frontiers_width[i], self.dimensions[i] - self.frontiers_width[i])
            for i in range(self.dimensions.size)
        )
        self.frontier_mask = np.ones(self.dimensions, dtype=bool)
        # el subshape no hace parte de la frontera
        self.frontier_mask[not_frotier] = 0

        self.attributes_number = attributes_number
        self.memory_length = memory_length

        # This is the index for the writing board
        self.writing_board = 0
        # this is the index for the reading board
        self.reading_board = memory_length - 1

    def __iter__(self) -> Type[NGridIterator]:
        return NGridIterator(self.dimensions, self.frontiers_width)

    def flip(self) -> None:
        self.writing_board += 1
        self.writing_board %= self.memory_length

        self.reading_board += 1
        self.reading_board %= self.memory_length

    def get_cell(
        self, position: Tuple[int, ...], board: int = None
    ) -> npt.NDArray[np.float]:
        board = board or self.reading_board
        return self.cells[board][(slice(None, None, None), *position)]

    def get_cells(
        self, subregion: Iterable[Tuple[int, int]] = None, board: int = None
    ) -> npt.NDArray[np.float]:
        board = board or self.reading_board
        cells = self.cells[board]
        if subregion is not None:
            index = [slice(i, f) for i, f in subregion]
            cells = self.cells[board][(slice(None, None, None), *index)]
        return cells

    def get_states(
        self, board: int = None, with_frontiers: bool = False
    ) -> npt.NDArray[np.float]:
        board = board or self.reading_board
        states = self.cells[board][0]
        if not with_frontiers:
            states = states[~self.frontier_mask].reshape(self.sub_dimensions)
        return states

    def get_attributes(
        self, board: int = None, with_frontiers: bool = False
    ) -> npt.NDArray[np.float]:
        board = board or self.reading_board
        attributes = self.cells[board][1:]
        if not with_frontiers:
            attributes = attributes[:, ~self.frontier_mask].reshape(
                (self.attributes_number, *self.sub_dimensions)
            )
        return attributes

    def set_cell_value(
        self,
        position: Tuple[int, ...],
        cell_state: int,
        cell_attributes: Optional[Union[List[float], npt.NDArray[np.float]]],
        board: int = None,
    ) -> None:
        board = board or self.writing_board
        self.cells[board][(slice(None, None, None), *position)] = [
            cell_state,
            *cell_attributes,
        ]

    def set_border_cell_values(
        self,
        cell_state: int,
        cell_attributes: Optional[Union[List[float], npt.NDArray[np.float]]],
        board: int = None,
    ) -> None:
        board = board or self.writing_board
        broadcast_dimension = (np.sum(self.frontier_mask), 1 + self.attributes_number)
        self.cells[board][:, self.frontier_mask] = np.broadcast_to(
            [cell_state, *cell_attributes], broadcast_dimension
        ).transpose()

    def set_cells_values(
        self,
        cell_state: int,
        cell_attributes: Optional[Union[List[float], npt.NDArray[np.float]]],
        subregion: Iterable[Tuple[int, int]] = None,
        board: int = None,
    ) -> None:
        board = board or self.writing_board

        index = slice(None, None, None)
        dimensions = self.dimensions
        if subregion is not None:
            index = [slice(None, None, None)]
            index.extend([slice(i, f) for i, f in subregion])
            index = tuple(index)
            dimensions = [f - i for i, f in subregion]

        output_shape = self.attributes_number + 1, *dimensions
        new_values = [cell_state, *cell_attributes]
        broadcast_dimension = np.product(dimensions), 1 + self.attributes_number

        self.cells[board][index] = (
            np.broadcast_to(new_values, broadcast_dimension)
            .transpose()
            .reshape(*output_shape)
        )

    def set_cells_state_values(
        self,
        cell_state: int,
        subregion: Iterable[Tuple[int, int]] = None,
        board: int = None,
    ) -> None:
        board = board or self.writing_board

        index = slice(0, 1)
        if subregion is not None:
            index = [slice(0, 1)]
            index.extend([slice(i, f) for i, f in subregion])
            index = tuple(index)

        self.cells[board][index] = cell_state

    def set_cells_attributes_values(
        self,
        cell_attributes: Optional[Union[List[float], npt.NDArray[np.float]]],
        subregion: Iterable[Tuple[int, int]] = None,
        board: int = None,
    ) -> None:
        board = board or self.writing_board

        index = slice(1, None)
        dimensions = self.dimensions
        if subregion is not None:
            index = [slice(1, None)]
            index.extend([slice(i, f) for i, f in subregion])
            index = tuple(index)
            dimensions = [f - i for i, f in subregion]

        output_shape = self.attributes_number, *dimensions
        broadcast_dimension = np.product(dimensions), self.attributes_number

        self.cells[board][index] = (
            np.broadcast_to(cell_attributes, broadcast_dimension)
            .transpose()
            .reshape(*output_shape)
        )

    def set_cells_states_from_array(
        self,
        data: npt.NDArray[np.float],
        subregion: Iterable[Tuple[int, int]] = None,
        board: int = None,
    ) -> None:
        board = board or self.writing_board

        index = slice(0, 1)
        if subregion is not None:
            index = [slice(0, 1)]
            index.extend([slice(i, f) for i, f in subregion])
            index = tuple(index)

        self.cells[board][index] = data

    def set_cells_attributes_from_array(
        self,
        data: npt.NDArray[np.float],
        subregion: Iterable[Tuple[int, int]] = None,
        board: int = None,
    ) -> None:
        board = board or self.writing_board

        index = slice(1, None, None)
        if subregion is not None:
            index = [slice(1, None, None)]
            index.extend([slice(i, f) for i, f in subregion])
            index = tuple(index)

        self.cells[board][index] = data

    def set_cells_from_array(
        self,
        data: npt.NDArray[np.float],
        subregion: Iterable[Tuple[int, int]] = None,
        board: int = None,
    ) -> None:
        board = board or self.writing_board

        index = slice(None, None, None)
        if subregion is not None:
            index = [slice(None, None, None)]
            index.extend([slice(i, f) for i, f in subregion])
            index = tuple(index)

        self.cells[board][index] = data

    def apply_mask(
        self, position: Tuple[int, ...], mask: npt.NDArray[np.int]
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
