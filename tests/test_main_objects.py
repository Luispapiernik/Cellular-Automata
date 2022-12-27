"""
En este script se testean objetos iniciales (que no dependen de
ninguna caracteristica particular de cualquier automata, como la dimensiona-
lidad, ...), esto es, en general aquellos cuya implementacion esta en
./pycellslib/__init__.py
"""

import unittest

import numpy as np

from pycellslib.cells import StandardCell
from pycellslib.core import FiniteNGridTopology
from pycellslib.errors import (
    InitializationWithoutParametersError,
    InvalidParameterError,
)
from pycellslib.utils import PositionIterator


class TestStandardCell(unittest.TestCase):
    """
    Tests para la clase StandardCell

    Esta clase hereda de una clase abstracta, entonces en el proceso
    implicitamente se esta testeando que se hayan definido todos los metodos
    de la clase padre y que tengan un funcionamiento correcto
    """

    @unittest.skip("Implementando funcionalidad")
    def test_initialization_without_parameters(self):
        """
        Este metodo testea el caso en el que se inicialice StandardCell sin
        pasar parametros
        """
        msg = "No se puede instanciar StandardCell sin parametros"
        with self.assertRaises(InitializationWithoutParametersError, msg=msg):
            StandardCell()

    @unittest.skip("Implementando funcionalidad")
    def test_initialization_with_invalid_default_state(self):
        """
        Este metodo testea el caso en el que se inicialice StandardCell con un
        default_state que no esta en los estados especificados
        """
        msg = "Parametro invalido, el valor especificado para default_state no es uno de los posibles estados"
        with self.assertRaises(InvalidParameterError, msg=msg):
            StandardCell(2, default_state=2)

    @unittest.skip("Implementando funcionalidad")
    def test_get_states_initialization_from_iterable_invalid_type(self):
        """
        Este metodo testea la inicializacion de StandardCell desde un iterable
        con valores de tipo diferente a entero
        """
        msg = "Parametro invalido, la lista debe ser de enteros"
        with self.assertRaises(InvalidParameterError, msg=msg):
            StandardCell([0.1, 2.4, "lo que sea"])

    def test_get_states_initialization_from_iterable(self):
        """
        Este metodo testea la inicializacion de StandardCell desde un iterable
        y el metodo get_states del objeto resultante
        """
        cell = StandardCell([0, 1, 2])

        # en esta linea se esta testeando implicitamente que el tipo retornado
        # sea list
        self.assertEqual(cell.get_states(), [0, 1, 2])

    def test_get_states_initialization_from_numbers_of_states(self):
        """
        Este metodo testea la inicializacion de StandardCell especificando solo
        el numero de estados y el metodo get_states del objeto resultante
        """
        cell = StandardCell(5)

        # en esta linea se esta testeando implicitamente que el tipo retornado
        # sea list
        self.assertEqual(cell.get_states(), [0, 1, 2, 3, 4])

    def test_get_states_initializatoin_from_range_of_states_1(self):
        """
        Este metodo testea la inicializacion de StandardCell especificando el
        rango en el que estan los estados y el metodo get_states del objeto
        resultante
        """
        cell = StandardCell(3, 8)

        # en esta linea se esta testeando implicitamente que el tipo retornado
        # sea list
        self.assertEqual(cell.get_states(), [3, 4, 5, 6, 7])

    def test_get_states_initializatoin_from_range_of_states_2(self):
        """
        Este metodo testea la inicializacion de StandardCell especificando el
        rango en el que estan los estados, ademas de una distancia entre los
        enteros y el metodo get_states del objeto resultante
        """
        cell = StandardCell(2, 12, 2)

        # en esta linea se esta testeando implicitamente que el tipo retornado
        # sea list
        self.assertEqual(cell.get_states(), [2, 4, 6, 8, 10])

    def test_get_default_state_when_is_specified(self):
        """
        Este metodo testea el metodo get_default_state cuando este es
        especificado
        """
        cell = StandardCell(2, default_state=1)

        self.assertEqual(cell.get_default_state(), 1)

    def test_get_default_state_when_is_not_specified(self):
        """
        Este metodo testea el metodo get_default_state cuando este no es
        especificado en la inicializacion
        """
        cell = StandardCell(2, 5)

        self.assertEqual(cell.get_default_state(), 2)

    def test_get_attributes_number(self):
        """
        Este metodo testea el metodo get_number_of_attributes de los objetos
        instancia de la clase StandardCell
        """
        cell = StandardCell(2)

        self.assertEqual(cell.get_attributes_number(), 0)

    def test_get_default_value_of_attributes(self):
        """
        Este metodo testea el metodo get_default_value_of_attributes
        """
        cell = StandardCell(2)

        self.assertEqual(cell.get_default_value_of_attributes(), [])

    def test_get_name_of_state_with_full_specifications_of_names(self):
        """
        Este metodo testea el metodo get_name_of_state cuando en la
        inicializacion se especificaron todos los nombres
        """
        cell = StandardCell(2, states_names=["Dead", "Alive"])

        self.assertEqual(cell.get_state_name(0), "Dead")
        self.assertEqual(cell.get_state_name(1), "Alive")

    @unittest.skip("Implementando funcionalidad")
    def test_get_name_of_state_non_existent_state(self):
        """
        Este metodo testea el metodo get_name_of_state cuando se pasa como
        argumento un estado que no esta en la lista de posibles estados
        """
        cell = StandardCell(2, name_of_states=["Dead", "Alive"])

        msg = "Parametro invalido, el estado especificado no es uno de los posibles estados"
        with self.assertRaises(InvalidParameterError, msg=msg):
            cell.get_name_of_state(2)

    def test_get_name_of_state_with_some_specifications_of_names(self):
        """
        Este metodo testea el metodo get_name_of_state cuando en la
        inicializacion se especifican los primeros nombres
        """
        cell = StandardCell(5, states_names=["Dead", "Alive", "Binary"])

        self.assertEqual(cell.get_state_name(0), "Dead")
        self.assertEqual(cell.get_state_name(1), "Alive")
        self.assertEqual(cell.get_state_name(2), "Binary")
        self.assertEqual(cell.get_state_name(3), "")
        self.assertEqual(cell.get_state_name(4), "")

    def test_get_name_of_state_without_specifications_of_names(self):
        """
        Este metodo testea el metodo get_name_of_state cuando en la
        inicializacion no se especifico ningun nombre
        """
        cell = StandardCell(6)

        self.assertEqual(cell.get_state_name(0), "")
        self.assertEqual(cell.get_state_name(1), "")
        self.assertEqual(cell.get_state_name(2), "")
        self.assertEqual(cell.get_state_name(3), "")
        self.assertEqual(cell.get_state_name(4), "")

    def test_get_name_of_attributes(self):
        """
        Este metodo testea el metodo get_name_of_attributes
        """
        cell = StandardCell(2)

        # este metodo por implementacion interna espera un argumento de tipo
        # entero, pero para la clase StandardCell este metodo no tiene ni
        # importancia, ni significado, entonces sea cual sea el arugmento que
        # se le pase, este debe retornar None (si es necesario pasarle algo)
        self.assertEqual(cell.get_attribute_name(0), "")

    def test_attributes_1(self):
        cell = StandardCell(
            3, attributes=[1, 2, 3], attributes_names=["", "density", "a"]
        )

        self.assertEqual(cell.get_attributes_number(), 3)
        self.assertEqual(cell.get_default_value_of_attributes(), [1, 2, 3])

        self.assertEqual(cell.get_attribute_name(0), "")
        self.assertEqual(cell.get_attribute_name(1), "density")
        self.assertEqual(cell.get_attribute_name(2), "a")


# class TestPositionIterator(unittest.TestCase):
#     """
#     Tests para la clase PositionIterator
#     """

#     # @unittest.skip("Implementando funcionalidad")
#     def test_iter_and_next_method_1_dimensional_case_1(self):
#         """
#         Este metodo testea el metodo __iter__ y __next__ en el caso de tener
#         un borde de longitud 3 y un espacio de longitud 10
#         """
#         # en los casos unidimensionales se deben tener 2 ejes, donde el primero
#         # solo tiene tamaño 1, y en el primer eje el grosor no significa nada
#         # por tante no se deberia permitir tener un grosor diferente de cero
#         # para el primer eje
#         # el grid unidimensional esta embebido en un espacio 2 dimensional
#         # por eso la primera componente vale 1
#         dimensions = np.array((1, 10), dtype=int)
#         # la primera componente no tiene significado, solo informa del
#         # embebimiento que se hace
#         border_widths = np.array((0, 3), dtype=int)

#         for (y_pos, x_pos) in PositionIterator(dimensions, border_widths):
#             # el primer eje en las dimensiones siempre vale 1, por tanto la
#             # coordenada en ese eje valdra siempre cero
#             self.assertEqual(y_pos, 0)

#             # todas las posiciones deben estar en un rango donde no se
#             # haga referencia a la frontera
#             self.assertLess(border_widths[1] - 1, x_pos)
#             self.assertLess(x_pos, dimensions[1] + border_widths[1])

#     # @unittest.skip("Implementando funcionalidad")
#     def test_iter_and_next_method_1_dimensional_case_2(self):
#         """
#         Este metodo testea el metodo __iter__ y __next__ en el caso de tener
#         un borde de longitud 5 y un espacio de longitud 1
#         """
#         # en los casos unidimensionales se deben tener 2 ejes, donde el primero
#         # solo tiene tamaño 1, y en el primer eje el grosor no significa nada
#         # por tante no se deberia permitir tener un grosor diferente de cero
#         # para el primer eje
#         dimensions = np.array((1, 1), dtype=int)
#         border_widths = np.array((0, 5), dtype=int)

#         for (y_pos, x_pos) in PositionIterator(dimensions, border_widths):
#             # el primer eje en las dimensiones siempre vale 1, por tanto la
#             # coordenada en ese eje valdra siempre cero
#             self.assertEqual(y_pos, 0)

#             # todas las posiciones deben estar en un rango donde no se
#             # haga referencia a la frontera
#             self.assertLess(border_widths[1] - 1, x_pos)
#             self.assertLess(x_pos, dimensions[1] + border_widths[1])

#     # @unittest.skip("Implementando funcionalidad")
#     def test_iter_and_next_method_1_dimensional_case_3(self):
#         """
#         Este metodo testea el metodo __iter__ en el caso de tener un borde de
#         longitud 0 y un espacio de longitud 1
#         """
#         # en los casos unidimensionales se deben tener 2 ejes, donde el primero
#         # solo tiene tamaño 1, y en el primer eje el grosor no significa nada
#         # por tante no se deberia permitir tener un grosor diferente de cero
#         # para el primer eje
#         dimensions = np.array((1, 1), dtype=int)
#         border_widths = np.array((0, 0), dtype=int)

#         for (y_pos, x_pos) in PositionIterator(dimensions, border_widths):
#             # el primer eje en las dimensiones siempre vale 1, por tanto la
#             # coordenada en ese eje valdra siempre cero
#             self.assertEqual(y_pos, 0)

#             # todas las posiciones deben estar en un rango donde no se
#             # haga referencia a la frontera
#             self.assertLess(border_widths[1] - 1, x_pos)
#             self.assertLess(x_pos, dimensions[1] + border_widths[1])

#     # @unittest.skip("Implementando funcionalidad")
#     def test_iter_and_next_method_2_dimensional_case_1(self):
#         """
#         Este metodo testea el metodo __iter__ y __next__ en el caso de tener
#         un espacio de dimensiones (4, 3) y una frontera de dimensiones (13, 10)
#         """
#         dimensions = np.array((4, 3), dtype=int)
#         border_widths = np.array((13, 10), dtype=int)

#         for (y_pos, x_pos) in PositionIterator(dimensions, border_widths):
#             # todas las posiciones deben estar en un rango donde no se
#             # haga referencia a la frontera
#             self.assertLess(border_widths[1] - 1, x_pos)
#             self.assertLess(x_pos, dimensions[1] + border_widths[1])

#             self.assertLess(border_widths[0] - 1, y_pos)
#             self.assertLess(y_pos, dimensions[0] + border_widths[0])

#     # @unittest.skip("Implementando funcionalidad")
#     def test_iter_and_next_method_2_dimensional_case_2(self):
#         """
#         Este metodo testea el metodo __iter__ y __next__ en el caso de tener
#         un espacio de dimensiones (1, 1) y una frontera de dimensiones (5, 5)
#         """
#         dimensions = np.array((1, 1), dtype=int)
#         border_widths = np.array((5, 5), dtype=int)

#         for (y_pos, x_pos) in PositionIterator(dimensions, border_widths):
#             # todas las posiciones deben estar en un rango donde no se
#             # haga referencia a la frontera
#             self.assertLess(border_widths[1] - 1, x_pos)
#             self.assertLess(x_pos, dimensions[1] + border_widths[1])

#             self.assertLess(border_widths[0] - 1, y_pos)
#             self.assertLess(y_pos, dimensions[0] + border_widths[0])

#     # @unittest.skip("Implementando funcionalidad")
#     def test_iter_and_next_method_2_dimensional_case_3(self):
#         """
#         Este metodo testea el metodo __iter__ y __next__ en el caso de tener
#         un espacio de dimensiones (1, 1) y una frontera de dimensiones (0, 5)
#         """
#         dimensions = np.array((1, 1), dtype=int)
#         border_widths = np.array((0, 5), dtype=int)

#         for (y_pos, x_pos) in PositionIterator(dimensions, border_widths):
#             # todas las posiciones deben estar en un rango donde no se
#             # haga referencia a la frontera
#             self.assertLess(border_widths[1] - 1, x_pos)
#             self.assertLess(x_pos, dimensions[1] + border_widths[1])

#             self.assertLess(border_widths[0] - 1, y_pos)
#             self.assertLess(y_pos, dimensions[0] + border_widths[0])

#     # @unittest.skip("Implementando funcionalidad")
#     def test_iter_and_next_method_2_dimensional_case_4(self):
#         """
#         Este metodo testea el metodo __iter__ y __next__ en el caso de tener
#         un espacio de dimensiones (1, 1) y una frontera de dimensiones (5, 5)
#         """
#         dimensions = np.array((10, 1), dtype=int)
#         border_widths = np.array((0, 0), dtype=int)

#         for (y_pos, x_pos) in PositionIterator(dimensions, border_widths):
#             # todas las posiciones deben estar en un rango donde no se
#             # haga referencia a la frontera
#             self.assertLess(border_widths[1] - 1, x_pos)
#             self.assertLess(x_pos, dimensions[1] + border_widths[1])

#             self.assertLess(border_widths[0] - 1, y_pos)
#             self.assertLess(y_pos, dimensions[0] + border_widths[0])


# class TestFinite1GridTopology(unittest.TestCase):
#     """
#     Tests para la clase FiniteNGridTopology en el caso 1 dimensional
#     """

#     # @unittest.skip("Implementando funcionalidad")
#     def test_update_cell_and_get_cell_and_flip_case_1(self):
#         """
#         Este metodo testea los metodos update_cell y get_cell explicitamente
#         e implicitamente se testea el metodo flip, en el caso en el que se
#         tiene 2 atributos para las celular un espacio de longitud 20 y una
#         frontera de grosor 10
#         """
#         attributes_number = 2
#         dimensions = (1, 20)
#         border_widths = (0, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         for position in topology:
#             # aleatoriamente se escogen nuevos valores para las celulas
#             state = np.random.randint(1, 100)
#             attributes = np.random.randn(attributes_number)
#             # se escribe en una de las celulas en la estructura de datos
#             # usada para la escritura
#             topology.update_cell(position, state, attributes)

#             # para leer de la estructura de datos en la que se actualizo la
#             # celula se deben invertir los papeles usando el metodo flip, asi
#             # la estructura de datos pasa a ser de lectura
#             topology.flip()
#             cell_state, cell_attributes = topology.get_cell(position)

#             self.assertEqual(state, cell_state)
#             self.assertTrue(np.allclose(attributes, cell_attributes, equal_nan=True))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_update_cell_and_get_cell_case_2(self):
#         """
#         Este metodo testea los metodos update_cell y get_cell explicitamente
#         e implicitamente se testea el metodo flip, en el caso en el que se
#         tiene 0 atributos para las celular un espacio de longitud 1 y una
#         frontera de grosor 10
#         """
#         attributes_number = 0
#         dimensions = (1, 1)
#         border_widths = (0, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         for position in topology:
#             # aleatoriamente se escogen nuevos valores para las celulas
#             state = np.random.randint(1, 100)
#             # el espacio tiene cero atributos por celula
#             attributes = None
#             # se escribe en una de las celulas en la estructura de datos
#             # usada para la escritura
#             topology.update_cell(position, state, attributes)

#             # para leer de la estructura de datos en la que se actualizo la
#             # celula se deben invertir los papeles usando el metodo flip, asi
#             # la estructura de datos pasa a ser de lectura
#             topology.flip()
#             cell_state, cell_attributes = topology.get_cell(position)

#             self.assertEqual(state, cell_state)
#             self.assertIsNone(cell_attributes)

#     # no se deberia permitir borde con dimension 0, cuando se implementen
#     # excepciones en la libreria este test deberia ser modificado para lanzar
#     # errores
#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_and_get_states_and_get_attributes_case_1(self):
#         """
#         Este metodo testea los metodos set_values_from, get_states y
#         get_attributes explicitamente e implicitamente se testea el metodo flip
#         en el caso de tener 0 atributos para las celulas, un espacio de
#         longitud 5 y un borde de longitud 0
#         """
#         attributes_number = 0
#         dimensions = (1, 5)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         topology.set_values_from(state, None)

#         states = np.zeros(dimensions, dtype=int) + state
#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_and_get_states_and_get_attributes_case_2(self):
#         """
#         Este metodo testea los metodos set_values_from, get_states y
#         get_attributes explicitamente e implicitamente se testea el metodo flip
#         en el caso de tener 2 atributos para las celulas, un espacio de
#         longitud 5 y un borde de longitud 10
#         """
#         attributes_number = 2
#         dimensions = (1, 5)
#         border_widths = (0, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         attributes = np.random.randn(attributes_number)
#         topology.set_values_from(state, attributes)

#         states = np.zeros(dimensions, dtype=int) + state
#         # el arreglo de atributos no debe necesariamente estar lleno de ceros
#         # en los bordes, se agrega aleatoriedad al sumar state
#         attributes_array = np.zeros((*dimensions, attributes_number)) + state
#         attributes_array[..., :] = attributes

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))
#         self.assertTrue(np.allclose(topology.get_attributes(), attributes_array))

#     # no se deberia permitir borde con dimension 0, cuando se implementen
#     # excepciones en la libreria este test deberia ser modificado para lanzar
#     # errores
#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_and_get_states_and_get_attributes_case_3(self):
#         """
#         Este metodo testea los metodos set_values_from, get_states y
#         get_attributes explicitamente e implicitamente se testea el metodo flip
#         en el caso de tener 5 atributos para las celulas, un espacio de
#         longitud 1 y un borde de longitud 0
#         """
#         attributes_number = 5
#         dimensions = (1, 1)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         attributes = np.random.randn(attributes_number)
#         topology.set_values_from(state, attributes)

#         states = np.zeros(dimensions, dtype=int) + state
#         # el arreglo de atributos no debe necesariamente estar lleno de ceros
#         # en los bordes, se agrega aleatoriedad al sumar state
#         attributes_array = np.zeros((*dimensions, attributes_number)) + state
#         attributes_array[..., :] = attributes

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))
#         self.assertTrue(np.allclose(topology.get_attributes(), attributes_array))

#     # no se deberia permitir borde con dimension 0, cuando se implementen
#     # excepciones en la libreria este test deberia ser modificado para lanzar
#     # errores
#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_configuration_case_1(self):
#         """
#         Este metodo testea el metodo set_values_from_configuration
#         explicitamente, e implicitamente se testeara get_states y
#         get_attributes para el caso de tener 0 atributos por celula un espacio
#         del longitud 5 y un borde de grosor 0
#         """
#         attributes_number = 0
#         dimensions = (1, 5)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         states = np.zeros(dimensions) + np.random.randint(1, 100)
#         # se tiene 0 atributos por celula
#         attributes = None
#         topology.set_values_from_configuration(states, attributes)

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_configuration_case_2(self):
#         """
#         Este metodo testea el metodo set_values_from_configuration
#         explicitamente, e implicitamente se testeara get_states y
#         get_attributes para el caso de tener 2 atributos por celula un espacio
#         del longitud 5 y un borde de grosor 10
#         """
#         attributes_number = 2
#         dimensions = (1, 5)
#         border_widths = (0, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         states = np.zeros(dimensions) + np.random.randint(1, 100)
#         attributes_array = np.random.random((*dimensions, attributes_number))
#         topology.set_values_from_configuration(states, attributes_array)

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))
#         self.assertTrue(np.allclose(topology.get_attributes(), attributes_array))

#     # no se deberia permitir borde con dimension 0, cuando se implementen
#     # excepciones en la libreria este test deberia ser modificado para lanzar
#     # errores
#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_configuration_case_3(self):
#         """
#         Este metodo testea el metodo set_values_from_configuration
#         explicitamente, e implicitamente se testeara get_states y
#         get_attributes para el caso de tener 5 atributos por celula un espacio
#         del longitud 1 y un borde de grosor 0
#         """
#         attributes_number = 5
#         dimensions = (1, 1)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         states = np.zeros(dimensions) + np.random.randint(1, 100)
#         attributes_array = np.random.random((*dimensions, attributes_number))
#         topology.set_values_from_configuration(states, attributes_array)

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))
#         self.assertTrue(np.allclose(topology.get_attributes(), attributes_array))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_apply_mask_case_1(self):
#         """
#         Este metodo testea el metodo apply_mask en el caso de tener 0 atributos
#         por celula, un espacio de longitud 10 y una frontera de longitud 3
#         """
#         attributes_number = 0
#         dimensions = (1, 10)
#         # no tiene sentido aplicar una mascara sin que halla borde, debe haber
#         # un grosor de borde, al menos de las dimensiones de la mascara
#         border_widths = (0, 3)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         states = np.expand_dims(np.arange(dimensions[1], dtype=int), axis=0)
#         topology.set_values_from_configuration(states, None)
#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip
#         topology.flip()

#         mask = np.array([[1, 1, 1]], dtype=bool)
#         neighborhoods = np.array(
#             [
#                 [0, 1, 2],
#                 [1, 2, 3],
#                 [2, 3, 4],
#                 [3, 4, 5],
#                 [4, 5, 6],
#                 [5, 6, 7],
#                 [6, 7, 8],
#                 [7, 8, 9],
#                 [8, 9, 0],
#                 [9, 0, 0],
#             ]
#         )

#         counter = 0
#         for position in topology:
#             states_n, attributes_n = topology.apply_mask(position, mask)

#             self.assertTrue(np.array_equal(states_n, neighborhoods[counter]))
#             self.assertIsNone(attributes_n)
#             counter += 1

#         # se recorrio todo el array de vecinos
#         self.assertEqual(counter, 10)

#     # @unittest.skip("Implementando funcionalidad")
#     def test_apply_mask_case_2(self):
#         """
#         Este metodo testea el metodo apply_mask en el caso de tener 2 atributos
#         por celula, un espacio de longitud 1 y una frontera de longitud 10
#         """
#         attributes_number = 2
#         dimensions = (1, 1)
#         border_widths = (0, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         attributes_array = np.random.random((*dimensions, attributes_number))
#         topology.set_values_from_configuration([[2]], attributes_array)
#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip
#         topology.flip()

#         mask = np.array([[1, 1, 1]], dtype=bool)
#         neighborhoods_1 = np.array([2, 0, 0], dtype=int)

#         neighborhoods_2 = np.array([attributes_array[0, 0], [0, 0], [0, 0]])

#         for position in topology:
#             states_n, attributes_n = topology.apply_mask(position, mask)

#             self.assertTrue(np.array_equal(states_n, neighborhoods_1))
#             self.assertTrue(np.array_equal(attributes_n, neighborhoods_2))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_border_values_case_1(self):
#         """
#         Este metodo testea el metodo set_border_values en caso de tener 0
#         atributos por celula, un espacio de longitud 7 y una frontera de
#         longitud 3
#         """
#         attributes_number = 0
#         dimensions = (1, 7)
#         border_widths = (0, 3)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         topology.set_border_values(state, None)

#         space = (
#             np.zeros(
#                 (
#                     dimensions[0] + 2 * border_widths[0],
#                     dimensions[1] + 2 * border_widths[1],
#                 ),
#                 dtype=int,
#             )
#             + state
#         )
#         space[0, border_widths[1] : border_widths[1] + dimensions[1]] = 0

#         self.assertTrue(np.array_equal(topology.states[topology.write_buffer], space))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_border_values_case_2(self):
#         """
#         Este metodo testea el metodo set_border_values en caso de tener 5
#         atributos por celula, un espacio de longitud 1 y una frontera de
#         longitud 7
#         """
#         attributes_number = 5
#         dimensions = (1, 1)
#         border_widths = (0, 7)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         attributes = np.random.randn(attributes_number)
#         topology.set_border_values(state, attributes)

#         space = (
#             np.zeros(
#                 (
#                     dimensions[0] + 2 * border_widths[0],
#                     dimensions[1] + 2 * border_widths[1],
#                 ),
#                 dtype=int,
#             )
#             + state
#         )
#         space[0, border_widths[1] : border_widths[1] + dimensions[1]] = 0

#         attributes_array = np.zeros(
#             (
#                 dimensions[0] + 2 * border_widths[0],
#                 dimensions[1] + 2 * border_widths[1],
#                 attributes_number,
#             )
#         )
#         attributes_array[..., :] = attributes
#         attributes_array[0, border_widths[1] : border_widths[1] + dimensions[1], :] = 0

#         self.assertTrue(np.array_equal(topology.states[topology.write_buffer], space))
#         self.assertTrue(
#             np.allclose(topology.attributes[topology.write_buffer], attributes_array)
#         )

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_border_values_case_3(self):
#         """
#         Este metodo testea el metodo set_border_values en caso de tener 2
#         atributos por celula, un espacio de longitud 10 y una frontera de
#         longitud 3
#         """
#         attributes_number = 2
#         dimensions = (1, 10)
#         border_widths = (0, 3)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         attributes = np.random.randn(attributes_number)
#         topology.set_border_values(state, attributes)

#         space = (
#             np.zeros(
#                 (
#                     dimensions[0] + 2 * border_widths[0],
#                     dimensions[1] + 2 * border_widths[1],
#                 ),
#                 dtype=int,
#             )
#             + state
#         )
#         space[0, border_widths[1] : border_widths[1] + dimensions[1]] = 0

#         attributes_array = np.zeros(
#             (
#                 dimensions[0] + 2 * border_widths[0],
#                 dimensions[1] + 2 * border_widths[1],
#                 attributes_number,
#             )
#         )
#         attributes_array[..., :] = attributes
#         attributes_array[0, border_widths[1] : border_widths[1] + dimensions[1], :] = 0

#         self.assertTrue(np.array_equal(topology.states[topology.write_buffer], space))
#         self.assertTrue(
#             np.allclose(topology.attributes[topology.write_buffer], attributes_array)
#         )


# class TestFinite2GridTopology(unittest.TestCase):
#     """
#     Tests para la clase FiniteNGridTopology en el caso 2 dimensional
#     """

#     # @unittest.skip("Implementando funcionalidad")
#     def test_update_cell_and_get_cell_and_flip_case_1(self):
#         """
#         Este metodo testea los metodos update_cell y get_cell explicitamente
#         e implicitamente se testea el metodo flip, en el caso en el que se
#         tiene 2 atributos para las celular un espacio de longitud 20 y una
#         frontera de grosor 10
#         """
#         attributes_number = 2
#         dimensions = (5, 20)
#         border_widths = (1, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         for position in topology:
#             # aleatoriamente se escogen nuevos valores para las celulas
#             state = np.random.randint(1, 100)
#             attributes = np.random.randn(attributes_number)
#             # se escribe en una de las celulas en la estructura de datos
#             # usada para la escritura
#             topology.update_cell(position, state, attributes)

#             # para leer de la estructura de datos en la que se actualizo la
#             # celula se deben invertir los papeles usando el metodo flip, asi
#             # la estructura de datos pasa a ser de lectura
#             topology.flip()
#             cell_state, cell_attributes = topology.get_cell(position)

#             self.assertEqual(state, cell_state)
#             self.assertTrue(np.allclose(attributes, cell_attributes, equal_nan=True))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_update_cell_and_get_cell_case_2(self):
#         """
#         Este metodo testea los metodos update_cell y get_cell explicitamente
#         e implicitamente se testea el metodo flip, en el caso en el que se
#         tiene 0 atributos para las celular un espacio de dimension (5, 5) y
#         una frontera de dimension (3, 10)
#         """
#         attributes_number = 0
#         dimensions = (5, 5)
#         border_widths = (3, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         for position in topology:
#             # aleatoriamente se escogen nuevos valores para las celulas
#             state = np.random.randint(1, 100)
#             attributes = None
#             # se escribe en una de las celulas en la estructura de datos
#             # usada para la escritura
#             topology.update_cell(position, state, attributes)

#             # para leer de la estructura de datos en la que se actualizo la
#             # celula se deben invertir los papeles usando el metodo flip, asi
#             # la estructura de datos pasa a ser de lectura
#             topology.flip()
#             cell_state, cell_attributes = topology.get_cell(position)

#             self.assertEqual(state, cell_state)
#             self.assertIsNone(cell_attributes)

#     # no se deberia permitir borde con dimension 0, cuando se implementen
#     # excepciones en la libreria este test deberia ser modificado para lanzar
#     # errores
#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_and_get_states_and_get_attributes_case_1(self):
#         """
#         Este metodo testea los metodos set_values_from, get_states y
#         get_attributes explicitamente e implicitamente se testea el metodo flip
#         en el caso de tener 0 atributos para las celulas, un espacio de
#         dimensiones (3, 5) y una frontera de dimensiones (0, 0)
#         """
#         attributes_number = 0
#         dimensions = (3, 5)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         topology.set_values_from(state, None)

#         states = np.zeros(dimensions, dtype=int) + state
#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_and_get_states_and_get_attributes_case_2(self):
#         """
#         Este metodo testea los metodos set_values_from, get_states y
#         get_attributes explicitamente e implicitamente se testea el metodo flip
#         en el caso de tener 2 atributos para las celulas, un espacio de
#         dimensiones (3, 5) y una frontera de dimensiones (0, 10)
#         """
#         attributes_number = 2
#         dimensions = (3, 5)
#         border_widths = (0, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         attributes = np.random.randn(attributes_number)
#         topology.set_values_from(state, attributes)

#         states = np.zeros(dimensions, dtype=int) + state
#         # el arreglo de atributos no debe necesariamente estar lleno de ceros
#         # en los bordes, se agrega aleatoriedad al sumar state
#         attributes_array = np.zeros((*dimensions, attributes_number)) + state
#         attributes_array[..., :] = attributes

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))
#         self.assertTrue(np.allclose(topology.get_attributes(), attributes_array))

#     # no se deberia permitir borde con dimension 0, cuando se implementen
#     # excepciones en la libreria este test deberia ser modificado para lanzar
#     # errores
#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_and_get_states_and_get_attributes_case_3(self):
#         """
#         Este metodo testea los metodos set_values_from, get_states y
#         get_attributes explicitamente e implicitamente se testea el metodo flip
#         en el caso de tener 5 atributos para las celulas, un espacio de
#         dimensiones (2, 2) y una frontera de dimensiones (0, 0)
#         """
#         attributes_number = 5
#         dimensions = (2, 2)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         attributes = np.random.randn(attributes_number)
#         topology.set_values_from(state, attributes)

#         states = np.zeros(dimensions, dtype=int) + state
#         # el arreglo de atributos no debe necesariamente estar lleno de ceros
#         # en los bordes, se agrega aleatoriedad al sumar state
#         attributes_array = np.zeros((*dimensions, attributes_number)) + state
#         attributes_array[..., :] = attributes

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))
#         self.assertTrue(np.allclose(topology.get_attributes(), attributes_array))

#     # no se deberia permitir borde con dimension 0, cuando se implementen
#     # excepciones en la libreria este test deberia ser modificado para lanzar
#     # errores
#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_configuration_case_1(self):
#         """
#         Este metodo testea el metodo set_values_from_configuration
#         explicitamente, e implicitamente se testeara get_states y
#         get_attributes para el caso de tener 0 atributos por celula un espacio
#         de dimensiones (10, 5) y una frontera de dimensiones (0, 0)
#         """
#         attributes_number = 0
#         dimensions = (10, 5)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         states = np.zeros(dimensions) + np.random.randint(1, 100)
#         # se tiene 0 atributos por celula
#         attributes = None
#         topology.set_values_from_configuration(states, attributes)

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_configuration_case_2(self):
#         """
#         Este metodo testea el metodo set_values_from_configuration
#         explicitamente, e implicitamente se testeara get_states y
#         get_attributes para el caso de tener 2 atributos por celula un espacio
#         de dimensiones (1, 5) y una frontera de dimensiones (0, 10)
#         """
#         attributes_number = 2
#         dimensions = (1, 5)
#         border_widths = (0, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         states = np.zeros(dimensions) + np.random.randint(1, 100)
#         attributes_array = np.random.random((*dimensions, attributes_number))
#         topology.set_values_from_configuration(states, attributes_array)

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))
#         self.assertTrue(np.allclose(topology.get_attributes(), attributes_array))

#     # no se deberia permitir borde con dimension 0, cuando se implementen
#     # excepciones en la libreria este test deberia ser modificado para lanzar
#     # errores
#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_values_from_configuration_case_3(self):
#         """
#         Este metodo testea el metodo set_values_from_configuration
#         explicitamente, e implicitamente se testeara get_states y
#         get_attributes para el caso de tener 5 atributos por celula un espacio
#         de dimensiones (20, 20) y una frontera de dimensiones (0, 0)
#         """
#         attributes_number = 5
#         dimensions = (20, 20)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         states = np.zeros(dimensions) + np.random.randint(1, 100)
#         attributes_array = np.random.random((*dimensions, attributes_number))
#         topology.set_values_from_configuration(states, attributes_array)

#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip, asi
#         # la estructura de datos pasa a ser de lectura
#         topology.flip()
#         self.assertTrue(np.array_equal(topology.get_states(), states))
#         self.assertTrue(np.allclose(topology.get_attributes(), attributes_array))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_border_values_case_1(self):
#         """
#         Este metodo testea el metodo set_border_values en caso de tener 0
#         atributos por celula, un espacio de dimensiones (4, 7) y una frontera
#         de dimensiones (0, 3)
#         """
#         attributes_number = 0
#         dimensions = (4, 7)
#         border_widths = (0, 3)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         topology.set_border_values(state, None)

#         space = (
#             np.zeros(
#                 (
#                     dimensions[0] + 2 * border_widths[0],
#                     dimensions[1] + 2 * border_widths[1],
#                 ),
#                 dtype=int,
#             )
#             + state
#         )
#         space[
#             border_widths[0] : border_widths[0] + dimensions[0],
#             border_widths[1] : border_widths[1] + dimensions[1],
#         ] = 0

#         self.assertTrue(np.array_equal(topology.states[topology.write_buffer], space))

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_border_values_case_2(self):
#         """
#         Este metodo testea el metodo set_border_values en caso de tener 5
#         atributos por celula, un espacio de longitud 1 y una frontera de
#         longitud 7
#         """
#         attributes_number = 5
#         dimensions = (10, 10)
#         border_widths = (12, 7)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         attributes = np.random.randn(attributes_number)
#         topology.set_border_values(state, attributes)

#         space = (
#             np.zeros(
#                 (
#                     dimensions[0] + 2 * border_widths[0],
#                     dimensions[1] + 2 * border_widths[1],
#                 ),
#                 dtype=int,
#             )
#             + state
#         )
#         space[
#             border_widths[0] : border_widths[0] + dimensions[0],
#             border_widths[1] : border_widths[1] + dimensions[1],
#         ] = 0

#         attributes_array = np.zeros(
#             (
#                 dimensions[0] + 2 * border_widths[0],
#                 dimensions[1] + 2 * border_widths[1],
#                 attributes_number,
#             )
#         )
#         attributes_array[..., :] = attributes
#         attributes_array[
#             border_widths[0] : border_widths[0] + dimensions[0],
#             border_widths[1] : border_widths[1] + dimensions[1],
#             :,
#         ] = 0

#         self.assertTrue(np.array_equal(topology.states[topology.write_buffer], space))
#         self.assertTrue(
#             np.allclose(topology.attributes[topology.write_buffer], attributes_array)
#         )

#     # @unittest.skip("Implementando funcionalidad")
#     def test_set_border_values_case_3(self):
#         """
#         Este metodo testea el metodo set_border_values en caso de tener 2
#         atributos por celula, un espacio de longitud 10 y una frontera de
#         longitud 3
#         """
#         attributes_number = 2
#         dimensions = (15, 10)
#         border_widths = (0, 0)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         state = np.random.randint(1, 100)
#         attributes = np.random.randn(attributes_number)
#         topology.set_border_values(state, attributes)

#         space = (
#             np.zeros(
#                 (
#                     dimensions[0] + 2 * border_widths[0],
#                     dimensions[1] + 2 * border_widths[1],
#                 ),
#                 dtype=int,
#             )
#             + state
#         )
#         space[
#             border_widths[0] : border_widths[0] + dimensions[0],
#             border_widths[1] : border_widths[1] + dimensions[1],
#         ] = 0

#         attributes_array = np.zeros(
#             (
#                 dimensions[0] + 2 * border_widths[0],
#                 dimensions[1] + 2 * border_widths[1],
#                 attributes_number,
#             )
#         )
#         attributes_array[..., :] = attributes
#         attributes_array[
#             border_widths[0] : border_widths[0] + dimensions[0],
#             border_widths[1] : border_widths[1] + dimensions[1],
#             :,
#         ] = 0

#         self.assertTrue(np.array_equal(topology.states[topology.write_buffer], space))
#         self.assertTrue(
#             np.allclose(topology.attributes[topology.write_buffer], attributes_array)
#         )

#     # @unittest.skip("Implementando funcionalidad")
#     def test_apply_mask_case_1(self):
#         """
#         Este metodo testea el metodo apply_mask en el caso de tener 0 atributos
#         por celula, un espacio de longitud 10 y una frontera de longitud 3
#         """
#         attributes_number = 0
#         dimensions = (3, 3)
#         # no tiene sentido aplicar una mascara sin que halla borde, debe haber
#         # un grosor de borde, al menos de las dimensiones de la mascara
#         border_widths = (2, 2)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         states = np.arange(9, dtype=int).reshape((3, 3))
#         topology.set_values_from_configuration(states, None)
#         topology.set_border_values(0, None)
#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip
#         topology.flip()

#         mask = np.array([[1, 1], [1, 1]], dtype=bool)
#         neighborhoods = np.array(
#             [
#                 [0, 1, 3, 4],
#                 [1, 2, 4, 5],
#                 [2, 0, 5, 0],
#                 [3, 4, 6, 7],
#                 [4, 5, 7, 8],
#                 [5, 0, 8, 0],
#                 [6, 7, 0, 0],
#                 [7, 8, 0, 0],
#                 [8, 0, 0, 0],
#             ]
#         )

#         counter = 0
#         for position in topology:
#             states_n, attributes_n = topology.apply_mask(position, mask)

#             self.assertTrue(np.array_equal(states_n, neighborhoods[counter]))
#             self.assertIsNone(attributes_n)
#             counter += 1

#         # se recorrio todo el array de vecinos
#         self.assertEqual(counter, 9)

#     # @unittest.skip("Implementando funcionalidad")
#     def test_apply_mask_case_2(self):
#         """
#         Este metodo testea el metodo apply_mask en el caso de tener 2 atributos
#         por celula, un espacio de longitud 1 y una frontera de longitud 10
#         """
#         attributes_number = 2
#         dimensions = (2, 2)
#         border_widths = (4, 10)
#         topology = FiniteNGridTopology(
#             attributes_number=attributes_number,
#             dimensions=dimensions,
#             border_widths=border_widths,
#         )

#         topology.set_values_from(1, [1, 1])
#         topology.set_border_values(1, [1, 1])
#         # para leer de la estructura de datos en la que se actualizaron las
#         # celulas se deben invertir los papeles usando el metodo flip
#         topology.flip()

#         mask = np.array([[1, 1], [1, 1]], dtype=bool)
#         neighborhoods_1 = np.array([1, 1, 1, 1], dtype=int)

#         neighborhoods_2 = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])

#         counter = 0
#         for position in topology:
#             states_n, attributes_n = topology.apply_mask(position, mask)

#             self.assertTrue(np.array_equal(states_n, neighborhoods_1))
#             self.assertTrue(np.array_equal(attributes_n, neighborhoods_2))

#             counter += 1

#         self.assertEqual(counter, 4)


if __name__ == "__main__":
    unittest.main()
