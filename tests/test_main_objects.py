"""
En este script se testean objetos iniciales (que no dependen de
ninguna caracteristica particular de cualquier automata, como la dimensiona-
lidad, ...), esto es, en general aquellos cuya implementacion esta en
./pycellslib/__init__.py
"""

import unittest

from pycellslib.cells import StandardCell


class TestStandardCell(unittest.TestCase):
    """
    Test para la clase StandardCell

    Esta clase hereda de una clase abstracta, entonces en el proceso se debe
    testear tanto que se hayan definido todos los metodos de la clase padre y
    que tengan un funcionamiento correcto
    """

    # def test_initialization_without_parameters(self):
    #     """
    #     Este metodo testea el caso en el que se inicialice StandardCell sin
    #     pasar parametros
    #     """
    #     msg = 'No se puede instanciar StandardCell sin parametros'
    #     with self.assertRaises(InitializationWithoutParametersError, msg=msg):
    #         StandardCell()

    # def test_initialization_with_invalid_default_state(self):
    #     """
    #     Este metodo testea el caso en el que se inicialice StandardCell con un
    #     default_state que no esta en los estados especificados
    #     """
    #     msg = 'Parametro invalido, el valor especificado para default_state no es uno de los posibles estados'
    #     with self.assertRaises(InvalidParameterError, msg=msg):
    #         StandardCell(2, default_state=2)

    # def test_get_states_initialization_from_iterable_invalid_type(self):
    #     """
    #     Este metodo testea la inicializacion de StandardCell desde un iterable
    #     con valores de tipo diferente a entero
    #     """
    #     msg = 'Parametro invalido, la lista debe ser de enteros'
    #     with self.assertRaises(InvalidParameterError, msg=msg):
    #         StandardCell([0.1, 2.4, 'lo que sea'])

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

    # def test_get_name_of_state_non_existent_state(self):
    #     """
    #     Este metodo testea el metodo get_name_of_state cuando se pasa como
    #     argumento un estado que no esta en la lista de posibles estados
    #     """
    #     cell = StandardCell(2, name_of_states=['Dead', 'Alive'])

    #     msg = 'Parametro invalido, el estado especificado no es uno de los posibles estados'
    #     with self.assertRaises(InvalidParameterError, msg=msg):
    #         cell.get_name_of_state(2)

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


if __name__ == '__main__':
    unittest.main()
