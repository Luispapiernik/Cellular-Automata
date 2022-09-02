from abc import ABCMeta, abstractmethod


class Rule(metaclass=ABCMeta):
    """
    Una regla representa el como cambia el estado de cada celula, esto es,
    representa la vecindad y la funcion de transicion que se aplica a la
    vecindad
    """

    @abstractmethod
    def get_neighborhood(self):
        """
        Este metodo retorna la vecindad asociada a la regla

        Returns
        -------
        out(Neighborhood): Objeto que representa la vecindad
        """

    @abstractmethod
    def apply_rule(self, cell_states, cell_attributes):
        """
        Este metodo aplica las reglas de transicion a una vecindad de la
        celula

        Parameters
        ----------
        cell_states(ndarray(int)): arreglo que representa los estados de la
            vecindad de una celula (es retornado por el metodo apply_mask de
            la clase topology)
        cell_attributes(ndarray(float)): arreglo que representa los atributos
            de la vecindad de una celula (es retornado por el metodo apply_mask
            de la clase topology)

        Returns
        -------
        out(int|ndarray|list): representa el valor del estado de la celula y
            posiblemente el valor de los atributos de la celula. En caso de
            retornar valor de tipo ndarray o list, entonces la primera
            componente debe ser el valor del estado y las demas componentes,
            los valores de los atributos
        """
