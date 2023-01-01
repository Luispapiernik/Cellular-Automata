from abc import ABCMeta, abstractmethod
from typing import Tuple, Type, TypeVar

import numpy as np
import numpy.typing as npt

PIterator = TypeVar("PIterator", bound="PositionIterator")


class PositionIterator(ABCMeta):
    @abstractmethod
    def __iter__(self) -> Type[PIterator]:
        """"""

    @abstractmethod
    def __next__(self) -> Tuple[int, ...]:
        """"""


class NGridIterator(PositionIterator):
    def __init__(
        self, dimensions: npt.NDArray[np.int], frontiers_width: npt.NDArray[np.int]
    ) -> None:
        self.dimensions = dimensions
        self.frontiers_width = frontiers_width
        self.index = np.ndindex(*(dimensions + frontiers_width))

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[int, ...]:
        while True:
            # se revisa que las coordenadas esten en el limite permitido
            coordinate = np.array(next(self.index), dtype=int)

            inferior_limit = self.frontiers_width - 1 < coordinate
            superior_limit = coordinate < self.dimensions - self.frontiers_width

            if np.all(inferior_limit & superior_limit):
                return tuple(coordinate)
