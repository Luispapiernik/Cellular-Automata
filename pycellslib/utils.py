import numpy as np
import numpy.typing as npt


class PositionIterator:
    """
    Esta clase representa un iterador sobre posiciones permitidas en el
    espacio

    Parameters
    ----------
    dimensions(ndarray(int)): dimensiones del espacio
    border_widths(ndarray(int)): dimensiones de la frontera del espacio
    """

    def __init__(
        self, dimensions: npt.NDArray[np.int], border_widths: npt.NDArray[np.int]
    ) -> None:
        self.dimensions = dimensions
        # dimensiones de la frontera
        self.border_widths = border_widths

        self.index = np.ndindex(*(self.dimensions + self.border_widths))

    def __iter__(self) -> "PositionIterator":
        return self

    def __next__(self) -> npt.NDArray[np.int]:
        """
        Este metodo itera sobre todos los posibles indices del espacio y
        retorna solo aquellos que no corresponden a puntos de la frontera
        """
        while True:
            # se revisa que las coordenadas esten en el limite permitido
            coordinate = np.array(next(self.index), dtype=int)

            inferior_limit = self.border_widths - 1 < coordinate
            superior_limit = coordinate < self.dimensions + self.border_widths

            if np.all(inferior_limit & superior_limit):
                return tuple(coordinate)

        return coordinate
