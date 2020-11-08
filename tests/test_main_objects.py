"""
En este script se testean objetos iniciales (que no dependen de
ninguna caracteristica particular de cualquier automata, como la dimensiona-
lidad, ...), esto es, en general aquellos cuya implementacion esta en
./pycellslib/__init__.py
"""

import unittest
import numpy as np

from pycellslib import InitializationWithoutParametersError
from pycellslib import InvalidParameterError
from pycellslib.cells import StandardCell
from pycellslib import FiniteNGridTopology


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
        msg = 'No se puede instanciar StandardCell sin parametros'
        with self.assertRaises(InitializationWithoutParametersError, msg=msg):
            StandardCell()

    @unittest.skip("Implementando funcionalidad")
    def test_initialization_with_invalid_default_state(self):
        """
        Este metodo testea el caso en el que se inicialice StandardCell con un
        default_state que no esta en los estados especificados
        """
        msg = 'Parametro invalido, el valor especificado para default_state no es uno de los posibles estados'
        with self.assertRaises(InvalidParameterError, msg=msg):
            StandardCell(2, default_state=2)

    @unittest.skip("Implementando funcionalidad")
    def test_get_states_initialization_from_iterable_invalid_type(self):
        """
        Este metodo testea la inicializacion de StandardCell desde un iterable
        con valores de tipo diferente a entero
        """
        msg = 'Parametro invalido, la lista debe ser de enteros'
        with self.assertRaises(InvalidParameterError, msg=msg):
            StandardCell([0.1, 2.4, 'lo que sea'])

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

    def test_get_number_of_attributes(self):
        """
        Este metodo testea el metodo get_number_of_attributes de los objetos
        instancia de la clase StandardCell
        """
        cell = StandardCell(2)

        self.assertEqual(cell.get_number_of_attributes(), 0)

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

    def test_get_default_value_of_attributes(self):
        """
        Este metodo testea el metodo get_default_value_of_attributes
        """
        cell = StandardCell(2)

        self.assertIsNone(cell.get_default_value_of_attributes())

    @unittest.skip("Implementando funcionalidad")
    def test_get_name_of_state_non_existent_state(self):
        """
        Este metodo testea el metodo get_name_of_state cuando se pasa como
        argumento un estado que no esta en la lista de posibles estados
        """
        cell = StandardCell(2, name_of_states=['Dead', 'Alive'])

        msg = 'Parametro invalido, el estado especificado no es uno de los posibles estados'
        with self.assertRaises(InvalidParameterError, msg=msg):
            cell.get_name_of_state(2)

    def test_get_name_of_state_with_full_specifications_of_names(self):
        """
        Este metodo testea el metodo get_name_of_state cuando en la
        inicializacion se especificaron todos los nombres
        """
        cell = StandardCell(2, name_of_states=['Dead', 'Alive'])

        self.assertEqual(cell.get_name_of_state(0), 'Dead')
        self.assertEqual(cell.get_name_of_state(1), 'Alive')

    def test_get_name_of_state_with_some_specifications_of_names(self):
        """
        Este metodo testea el metodo get_name_of_state cuando en la
        inicializacion se especifican los primeros nombres
        """
        cell = StandardCell(5, name_of_states=['Dead', 'Alive', 'Binary'])

        self.assertEqual(cell.get_name_of_state(0), 'Dead')
        self.assertEqual(cell.get_name_of_state(1), 'Alive')
        self.assertEqual(cell.get_name_of_state(2), 'Binary')
        self.assertEqual(cell.get_name_of_state(3), '')
        self.assertEqual(cell.get_name_of_state(4), '')

    def test_get_name_of_state_without_specifications_of_names(self):
        """
        Este metodo testea el metodo get_name_of_state cuando en la
        inicializacion no se especifico ningun nombre
        """
        cell = StandardCell(6)

        self.assertEqual(cell.get_name_of_state(0), '')
        self.assertEqual(cell.get_name_of_state(1), '')
        self.assertEqual(cell.get_name_of_state(2), '')
        self.assertEqual(cell.get_name_of_state(3), '')
        self.assertEqual(cell.get_name_of_state(4), '')

    def test_get_name_of_attributes(self):
        """
        Este metodo testea el metodo get_name_of_attributes
        """
        cell = StandardCell(2)

        # este metodo por implementacion interna espera un argumento de tipo
        # entero, pero para la clase StandardCell este metodo no tiene ni
        # importancia, ni significado, entonces sea cual sea el arugmento que
        # se le pase, este debe retornar None (si es necesario pasarle algo)
        self.assertIsNone(cell.get_name_of_attributes(0))


class TestFinite1GridTopology(unittest.TestCase):
    """
    Tests para la clase FiniteNGridTopology en el caso 1 dimensional
    """

    # @unittest.skip("Implementando funcionalidad")
    def test_iter_case_1(self):
        """
        Este metodo testea el metodo __iter__ en el caso de tener un borde de
        longitud 3 y un espacio de longitud 3 y 0 atributos para las celulas
        """
        # en los casos unidimensionales se deben tener 2 ejes, donde el primero
        # solo tiene tamaño 1, y en el primer eje el grosor no significa nada
        # por tante no se deberia permitir tener un grosor diferente de cero
        # para el primer eje
        # el grid unidimensional esta embebido en un espacio 2 dimensional
        # por eso la primera componente vale 1
        dimensions = (1, 10)
        # la primera componente no tiene significado, solo informa del
        # embebimiento que se hace
        border_widths = (0, 3)
        topology = FiniteNGridTopology(attributes_number=0,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        # en este caso el iterador debe recorrer duplas con el indice de
        # cada celula
        for (y_pos, x_pos) in topology:
            # el primer eje en las dimensiones siempre vale 1, por tanto la
            # coordenada en ese eje valdra siempre cero
            self.assertEqual(y_pos, 0)

            # todas las posiciones deben estar en un rango donde no se
            # haga referencia a la frontera
            self.assertLess(border_widths[1] - 1, x_pos)
            self.assertLess(x_pos, dimensions[1] + border_widths[1])

    # @unittest.skip("Implementando funcionalidad")
    def test_iter_case_2(self):
        """
        Este metodo testea el metodo __iter__
        """
        # en los casos unidimensionales se deben tener 2 ejes, donde el primero
        # solo tiene tamaño 1, y en el primer eje el grosor no significa nada
        # por tante no se deberia permitir tener un grosor diferente de cero
        # para el primer eje
        dimensions = (1, 1)
        border_widths = (0, 5)
        topology = FiniteNGridTopology(attributes_number=1,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        for (y_pos, x_pos) in topology:
            self.assertEqual(y_pos, 0)

            # todas las posiciones deben estar en un rango donde no se
            # haga referencia a la frontera
            self.assertLess(border_widths[1] - 1, x_pos)
            self.assertLess(x_pos, dimensions[1] + border_widths[1])


    # @unittest.skip("Implementando funcionalidad")
    def test_iter_case_3(self):
        """
        Este metodo testea el metodo __iter__
        """
        # en los casos unidimensionales se deben tener 2 ejes, donde el primero
        # solo tiene tamaño 1, y en el primer eje el grosor no significa nada
        # por tante no se deberia permitir tener un grosor diferente de cero
        # para el primer eje
        dimensions = (1, 1)
        border_widths = (0, 0)
        topology = FiniteNGridTopology(attributes_number=2,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        for (y_pos, x_pos) in topology:
            self.assertEqual(y_pos, 0)

            # todas las posiciones deben estar en un rango donde no se
            # haga referencia a la frontera
            self.assertLess(border_widths[1] - 1, x_pos)
            self.assertLess(x_pos, dimensions[1] + border_widths[1])

    @unittest.skip("Implementando funcionalidad")
    def test_update_cell_and_get_cell_case_1(self):
        """
        Este metodo testea los metodos update_cell y get_cell
        """
        attributes_number = 2
        dimensions = (1, 20)
        border_widths = (0, 10)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        for position in topology:
            state = np.random.randint(1, 100)
            attributes = np.random.randn(attributes_number)
            topology.update_cell(position, state, attributes)

            cell_state, cell_attributes = topology.get_cell(position)

            self.assertEqual(state, cell_state)
            self.assertTrue(np.allclose(attributes, cell_attributes,
                                        equal_nan=True))

    @unittest.skip("Implementando funcionalidad")
    def test_update_cell_and_get_cell_case_2(self):
        """
        Este metodo testea los metodos update_cell y get_cell
        """
        attributes_number = 0
        dimensions = (1, 5)
        border_widths = (0, 10)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        for position in topology:
            state = np.random.randint(1, 100)
            topology.update_cell(position, state, None)

            cell_state, cell_attributes = topology.get_cell(position)

            self.assertEqual(state, cell_state)
            self.assertIsNone(cell_attributes)

    @unittest.skip("Implementando funcionalidad")
    def test_set_values_from_and_get_states_and_get_attributes_case_1(self):
        """
        Este metodo testea los metodos set_values_from, get_states y
        get_attributes
        """
        attributes_number = 0
        dimensions = (1, 5)
        border_widths = (0, 0)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        state = np.random.randint(1, 100)
        topology.set_values_from(state, None)

        states = np.zeros(dimensions) + state
        self.assertTrue(np.array_equal(topology.get_states(), states))

    @unittest.skip("Implementando funcionalidad")
    def test_set_values_from_and_get_states_and_get_attributes_case_2(self):
        """
        Este metodo testea los metodos set_values_from, get_states y
        get_attributes
        """
        attributes_number = 2
        dimensions = (1, 5)
        border_widths = (0, 10)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        state = np.random.randint(1, 100)
        attributes = np.random.randn(attributes_number)
        topology.set_values_from(state, attributes_number)

        states = np.zeros(dimensions) + state
        attributes_array = np.zeros((*dimensions, attributes_number))
        attributes_array[..., :] = attributes

        self.assertTrue(np.array_equal(topology.get_states(), states))
        self.assertTrue(np.allclose(topology.get_attributes(),
                                    attributes_array))

    @unittest.skip("Implementando funcionalidad")
    def test_set_values_from_and_get_states_and_get_attributes_case_3(self):
        """
        Este metodo testea los metodos set_values_from, get_states y
        get_attributes
        """
        attributes_number = 5
        dimensions = (1, 1)
        border_widths = (0, 0)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        state = np.random.randint(1, 100)
        attributes = np.random.randn(attributes_number)
        topology.set_values_from(state, attributes_number)

        states = np.zeros(dimensions) + state
        attributes_array = np.zeros((*dimensions, attributes_number))
        attributes_array[..., :] = attributes

        self.assertTrue(np.array_equal(topology.get_states(), states))
        self.assertTrue(np.allclose(topology.get_attributes(),
                                    attributes_array))

    @unittest.skip("Implementando funcionalidad")
    def test_set_values_from_configuration_case_1(self):
        """
        Este metodo testea el metodo set_values_from_configuration
        explicitamente, e implicitamente se testeara get_states y
        get_attributes
        """
        attributes_number = 0
        dimensions = (1, 5)
        border_widths = (0, 0)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        states = np.zeros(dimensions) + np.random.randint(1, 100)
        topology.set_values_from_configuration(states, None)

        self.assertTrue(np.array_equal(topology.get_states(), states))

    @unittest.skip("Implementando funcionalidad")
    def test_set_values_from_configuration_case_2(self):
        """
        Este metodo testea el metodo set_values_from_configuration
        explicitamente, e implicitamente se testeara get_states y
        get_attributes
        """
        attributes_number = 2
        dimensions = (1, 5)
        border_widths = (0, 10)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        states = np.zeros(dimensions) + np.random.randint(1, 100)
        attributes_array = np.random.random((*dimensions, attributes_number))
        topology.set_values_from_configuration(states, attributes_array)

        self.assertTrue(np.array_equal(topology.get_states(), states))
        self.assertTrue(np.allclose(topology.get_attributes(),
                                    attributes_array))

    @unittest.skip("Implementando funcionalidad")
    def test_set_values_from_configuration_case_3(self):
        """
        Este metodo testea el metodo set_values_from_configuration
        explicitamente, e implicitamente se testeara get_states y
        get_attributes
        """
        attributes_number = 5
        dimensions = (1, 1)
        border_widths = (0, 0)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        states = np.zeros(dimensions) + np.random.randint(1, 100)
        attributes_array = np.random.random((*dimensions, attributes_number))
        topology.set_values_from_configuration(states, attributes_array)

        self.assertTrue(np.array_equal(topology.get_states(), states))
        self.assertTrue(np.allclose(topology.get_attributes(),
                                    attributes_array))

    @unittest.skip("Implementando funcionalidad")
    def test_apply_mask_case_1(self):
        """
        Este metodo testea el metodo apply_mask
        """
        attributes_number = 0
        dimensions = (1, 10)
        # no tiene sentido aplicar una mascara sin que halla borde, debe haber
        # un grosor de borde, al menos de las dimensiones de la mascara
        border_widths = (0, 3)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        states = np.expand_dims(np.arange(dimensions[1], dtype=np.int))
        topology.set_values_from_configuration(states, None)

        mask = np.array([[1, 1, 1]], dtype=np.bool)
        neighborhoods = np.array([
            [[1, 2, 3]],
            [[2, 3, 4]],
            [[3, 4, 5]],
            [[4, 5, 6]],
            [[5, 6, 7]],
            [[6, 7, 8]],
            [[7, 8, 9]],
            [[8, 9, 0]],
            [[9, 0, 0]]
        ])

        counter = 1
        for position in topology:
            states_n, attributes_n = topology.apply_mask(position, mask)

            self.assertTrue(np.array_equal(states_n,
                            neighborhoods[counter]))
            self.assertIsNone(attributes_n)
            counter += 1

    @unittest.skip("Implementando funcionalidad")
    def test_apply_mask_case_2(self):
        """
        Este metodo testea el metodo apply_mask
        """
        attributes_number = 2
        dimensions = (1, 1)
        border_widths = (0, 10)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        states = np.expand_dims(np.arange(dimensions[1], dtype=np.int))
        attributes_array = np.random.random((*dimensions, attributes_number))
        topology.set_values_from_configuration(states, attributes_array)

        mask = np.array([[1, 1, 1]], dtype=np.bool)
        neighborhoods_1 = np.array([
            [[1, 2, 3]]
        ])

        neighborhoods_2 = np.vstack([attributes_array,
                                     np.zeros(2, 1, attributes_number)])

        counter = 1
        for position in topology:
            states_n, attributes_n = topology.apply_mask(position, mask)

            self.assertTrue(np.array_equal(states_n,
                            neighborhoods_1[counter]))
            self.assertTrue(np.array_equal(attributes_n,
                            neighborhoods_2))
            counter += 1

    @unittest.skip("Implementando funcionalidad")
    def test_set_border_values_case_1(self):
        """
        Este metodo testea el metodo set_border_values
        """
        attributes_number = 0
        dimensions = (1, 7)
        border_widths = (0, 3)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        state = np.random.randint(1, 100)
        topology.test_set_border_values(state, None)

        space = np.zeros(dimensions, dtype=np.int) + state
        space[0, border_widths[1]:border_widths[1] + dimensions[1]] = 0

        self.assertTrue(np.array_equal(topology.get_states(), space))

    @unittest.skip("Implementando funcionalidad")
    def test_set_border_values_case_2(self):
        """
        Este metodo testea el metodo set_border_values
        """
        attributes_number = 5
        dimensions = (1, 1)
        border_widths = (0, 7)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        state = np.random.randint(1, 100)
        attributes = np.random.randn(attributes_number)
        topology.test_set_border_values(state, attributes)

        space = np.zeros(dimensions, dtype=np.int) + state
        space[0, border_widths[1]:border_widths[1] + dimensions[1]] = 0
        attributes_array = np.zeros((*dimensions, attributes_number))
        attributes_array[..., :] = attributes
        attributes_array[0, border_widths[1]:border_widths[1] + dimensions[1], :] = 0

        self.assertTrue(np.array_equal(topology.get_states(), space))

    @unittest.skip("Implementando funcionalidad")
    def test_set_border_values_case_3(self):
        """
        Este metodo testea el metodo set_border_values
        """
        attributes_number = 2
        dimensions = (1, 10)
        border_widths = (0, 3)
        topology = FiniteNGridTopology(attributes_number=attributes_number,
                                       dimensions=dimensions,
                                       border_widths=border_widths)

        state = np.random.randint(1, 100)
        attributes = np.random.randn(attributes_number)
        topology.test_set_border_values(state, attributes)

        space = np.zeros(dimensions, dtype=np.int) + state
        space[0, border_widths[1]:border_widths[1] + dimensions[1]] = 0
        attributes_array = np.zeros((*dimensions, attributes_number))
        attributes_array[..., :] = attributes
        attributes_array[0, border_widths[1]:border_widths[1] + dimensions[1], :] = 0

        self.assertTrue(np.array_equal(topology.get_states(), space))


class TestFinite2GridTopology(unittest.TestCase):
    """
    Tests para la clase FiniteNGridTopology en el caso 2 dimensional
    """


if __name__ == '__main__':
    unittest.main()
