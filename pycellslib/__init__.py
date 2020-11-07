"""
Este modulo tendra la implementacion de objetos iniciales (que no dependen de
ninguna caracteristica particular de cualquier automata, como la dimensiona-
lidad, ...) tanto abstractos como no abstractos, estos son, aquellos que
codifican la informacion y comportamiento de las celulas (CellularInformation),
de la topologia (Topology, ...), de la vecindad (Neighborhood), la informacion
de las funciones de transicion y de como se relacionan todos estos objetos
entre si (con el objeto Automata)
"""

from abc import ABCMeta, abstractmethod


# class PyCellsLibError(Exception):
#     """
#     Esta clase solo tiene la intencion de renombrar (se crea un sinonimo), para
#     hacer mas claro que errores son creados en la libreria, todas las
#     excepciones deben heredar de esta clase
#     """


# class InitializationWithoutParametersError(PyCellsLibError):
#     """
#     Esta excepcion debe ser lanzada cuando se intente instanciar un objeto
#     sin pasar los parametros requeridos a la clase
#     """

#     def __init__(self, class_name):
#         msg = 'No se puede instanciar {} sin parametros'.format(class_name)
#         super().__init__(msg)


# class InvalidParameterError(PyCellsLibError):
#     """
#     Esta excepcion debe ser lanzada cuanto se pase un argumento invalido, esto
#     es, no esta en el rango requerido, no tenga el tipo adecuado, ...
#     """

#     def __init__(self, reason_msg):
#         msg = 'Parametro invalido, {}'.format(reason_msg)
#         super().__init__(msg)


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

        Params
        ------
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

        Params
        ------
        index(int): indice que corresponde al atributo

        Returns
        -------
        out(str|None): nombre del atributo, puede ser un string vacio
        """


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
    invierte los papeles en las estructuras de datos)
    """

    @abstractmethod
    def __iter__(self):
        """
        La clase Topology debe brindar una interfaz por la cual se pueda
        iterar por cada celula para realizar el proceso de actualizacion, este
        metodo retorna un iterador sobre las posiciones de las celulas
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
        como los atributos.
        """

    @abstractmethod
    def get_states(self):
        """
        Este metodo retorna los valores de los estados de las celulas

        Returns
        -------
        out(list(int)|tuple(int)|ndarray(int)): estados de las celulas
        """

    @abstractmethod
    def get_attributes(self):
        """
        Este metodo retorna los valores de los atributos de las celulas

        Returns
        -------
        out(list(int)|tuple(int)|ndarray(int)): atributos de las celulas
        """

    @abstractmethod
    def update_cell(self, position):
        """
        Este metodo se encarga de actualizar una celula
        """

    @abstractmethod
    def set_values_from_values(self, cell_state, cell_attributes):
        """
        Este metodo establece el valor de las celulas usando los mismos
        parametros tanto para los estados, como para los atributos
        """

    @abstractmethod
    def set_values_from_configuration(self, cell_states, cell_attributes):
        """
        Este metodo establece el valor de los estados y el valor de los
        atributos de las celulas
        """

    @abstractmethod
    def apply_mask(self, position):
        """
        Este metodo permite obtener una subregion del espacio (que generalmente
        corresponderan a la vecindad de una celula), esto es, se retorna la
        informacion de los estados y de los atributos
        """


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

        Params
        ------
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


class Automaton:
    """
    Un objeto de la clase Automaton encapsula la idea de automata, esta clase
    se encarga de coordinar las clases Cells, Topology y Rules, y ofrece
    metodos para la extraccion de informacion (densidades o de estados o de
    atributos, flujos, ...) del automata
    """

    def load_configuration(self, directory):
        """
        Este metodo debe cargar la informacion del automata desde un directorio
        """

    def save_configuration(self, directory):
        """
        Este metodo debe guardar toda la informacion que permita la
        reinstanciacion del automata en cualquier sistema
        """

    def get_density_of_state(self, state):
        """
        Este metodo obtiene la densidad de algun estado en todo el espacio
        """

    def get_densities_of_states(self):
        """
        Este metodo obtiene las densidades de todos los estados en todo el
        espacio
        """

    def get_average_of_attribute(self, index):
        """
        Este metodo obtiene el promedio del atributo especificado (por medio
        del indice) en todo el espacio
        """

    def get_averages_of_attributes(self):
        """
        Este metodo obtiene el promedio de todos los atributos en todo el
        espacio
        """

    def next_step(self):
        """
        Este metodo itera un paso en la ejecucion del automata
        """

class FiniteNGridTopology(Topology):
    """
    La topologia representa la informacion espacial de una automata, esto es,
    tiene encapsulada las dimensiones, la distribucion de las celulas, los
    valores de estados y atributos en cada parte del espacio, metodos
    que extraen y asignan valores a subregiones del espacio...

    Esta clase representa una topologia rectangular n-dimensional, esto es,
    para 2 dimensiones se puede visualizar como rectangulos, para 3 dimensiones
    como cubos, ...
    """

    def __init__(self, arg):
        pass

    def __iter__(self):
        """
        La clase Topology debe brindar una interfaz por la cual se pueda
        iterar por cada celula para realizar el proceso de actualizacion, este
        metodo retorna un iterador sobre las posiciones de las celulas
        """

    def flip(self):
        """
        Este metodo cambia el papel (ser de lectura o ser de escritura) que
        cumplen las 2 estructuras de datos en las que se almacenan la
        informacion de estados y atributos de las celulas
        """

    def get_cell(self, position):
        """
        Este metodo obtiene la informacion de una celula, tanto los estados
        como los atributos.
        """

    def get_states(self):
        """
        Este metodo retorna los valores de los estados de las celulas

        Returns
        -------
        out(list(int)|tuple(int)|ndarray(int)): estados de las celulas
        """

    def get_attributes(self):
        """
        Este metodo retorna los valores de los atributos de las celulas

        Returns
        -------
        out(list(int)|tuple(int)|ndarray(int)): atributos de las celulas
        """

    def update_cell(self, position):
        """
        Este metodo se encarga de actualizar una celula
        """

    def set_values_from_values(self, cell_state, cell_attributes):
        """
        Este metodo establece el valor de las celulas usando los mismos
        parametros tanto para los estados, como para los atributos
        """

    def set_values_from_configuration(self, cell_states, cell_attributes):
        """
        Este metodo establece el valor de los estados y el valor de los
        atributos de las celulas
        """

    def apply_mask(self, position):
        """
        Este metodo permite obtener una subregion del espacio (que generalmente
        corresponderan a la vecindad de una celula), esto es, se retorna la
        informacion de los estados y de los atributos
        """
