from abc import ABCMeta, abstractmethod


class Neighborhood(metaclass=ABCMeta):
    """
    El vecindario de una celula define que celulas condicionan como cambia de
    estado cuando se aplica la funcion de transicion. La vecindad de una celula
    se representa como una mascara (array de numpy de tipo bool), False indica
    que la celula no afecta, y True indica que la celula si afecta. Esta
    mascara se superpone en el array que contiene las celulas (en la clase
    Topology) usando como coordenadas la posicion de la celula en cuestion mas
    un offset (una translacion)
    """

    @abstractmethod
    def get_mask(self):
        """
        Este metodo retorna la mascara que define la vecindad de una celula

        Returns
        -------
        out(ndarray(bool)): mascara
        """

    @abstractmethod
    def get_offset(self):
        """
        Este metodo retorna el offset de la mascara

        Returns
        -------
        out(tuple(int)|list(int)|ndarray(int)): valor que indica el offset en
            cada eje de la mascara
        """
