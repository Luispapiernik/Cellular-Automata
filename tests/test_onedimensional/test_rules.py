"""
En este script se testea las reglas implementadas para los casos
bidimensionales
"""

import unittest
import numpy as np

from pycellslib.onedimensional.neighborhoods import DummyNeighborhood
from pycellslib.onedimensional.rules import WolframCodeRule


class TestWolframCodeRule(unittest.TestCase):
    """
    Tests para la clase WolframCodeRule
    """

    def test_get_neighborhood(self):
        """
        Este metodo testea el metodo get_neighborhood
        """
        # en este caso los argumentos son arbitrarios, no importan
        rule = WolframCodeRule(rule_number=0, states_number=2,
                               neighborhood_radius=1)

        # la vecindad debe heredar de DummyNeighborhood, porque puede ser
        # cualquiera de las siguientes: MooreNeighborhood, NeummanNeighborhood,
        # L2Neighborhood o CircularNeighborhood
        self.assertIsInstance(rule.get_neighborhood(), DummyNeighborhood)

    def test_get_max_rule_number_case_1(self):
        """
        Este metodo testea el metodo get_max_rule_number
        """
        rule = WolframCodeRule(rule_number=0, states_number=2,
                               neighborhood_radius=1)

        self.assertEqual(rule.get_max_rule_number(), 255)

    def test_get_max_rule_number_case_2(self):
        """
        Este metodo testea el metodo get_max_rule_number
        """
        rule = WolframCodeRule(rule_number=0, states_number=3,
                               neighborhood_radius=1)

        self.assertEqual(rule.get_max_rule_number(), 7625597484986)

    def test_get_base_representation_case_1(self):
        """
        Este metodo testea el metodo get_base_representation
        """
        rule = WolframCodeRule(rule_number=0, states_number=3,
                               neighborhood_radius=1)

        number = np.array([0] * (27 - 5) + [1, 1, 1, 2, 0], dtype=np.int)
        self.assertTrue(np.array_equal(rule.get_base_representation(123),
                                       number))

    def test_get_base_representation_case_2(self):
        """
        Este metodo testea el metodo get_base_representation
        """
        rule = WolframCodeRule(rule_number=0, states_number=2,
                               neighborhood_radius=1)

        number = np.array([0, 1, 1, 1, 1, 0, 1, 1], dtype=np.int)
        self.assertTrue(np.array_equal(rule.get_base_representation(123),
                                       number))

    def test_base_representation_to_int_case_1(self):
        """
        Este metodo testea el metodo base_representation_to_int
        """
        rule = WolframCodeRule(rule_number=0, states_number=2,
                               neighborhood_radius=1)

        number = np.array([1, 0, 1], dtype=np.int)
        self.assertEqual(rule.base_representation_to_int(number), 5)

    def test_base_representation_to_int_case_2(self):
        """
        Este metodo testea el metodo base_representation_to_int
        """
        rule = WolframCodeRule(rule_number=0, states_number=5,
                               neighborhood_radius=1)

        number = np.array([1, 1, 1], dtype=np.int)
        self.assertEqual(rule.base_representation_to_int(number), 31)

    def test_base_representation_to_int_case_3(self):
        """
        Este metodo testea el metodo base_representation_to_int
        """
        rule = WolframCodeRule(rule_number=0, states_number=4,
                               neighborhood_radius=2)

        number = np.array([0, 0, 1, 1, 0], dtype=np.int)
        self.assertEqual(rule.base_representation_to_int(number), 20)

    def test_apply_rule(self):
        """
        Este metodo testea el metodo apply_rule
        """
        rule = WolframCodeRule(rule_number=30, states_number=2,
                               neighborhood_radius=1)

        states = np.array([1, 1, 1], dtype=np.int)
        state, _ = rule.apply_rule(states, None)
        self.assertEqual(state, 0)

        states[:] = [1, 1, 0]
        state, _ = rule.apply_rule(states, None)
        self.assertEqual(state, 0)

        states[:] = [1, 0, 1]
        state, _ = rule.apply_rule(states, None)
        self.assertEqual(state, 0)

        states[:] = [1, 0, 0]
        state, _ = rule.apply_rule(states, None)
        self.assertEqual(state, 1)

        states[:] = [0, 1, 1]
        state, _ = rule.apply_rule(states, None)
        self.assertEqual(state, 1)

        states[:] = [0, 1, 0]
        state, _ = rule.apply_rule(states, None)
        self.assertEqual(state, 1)

        states[:] = [0, 0, 1]
        state, _ = rule.apply_rule(states, None)
        self.assertEqual(state, 1)

        states[:] = [0, 0, 0]
        state, _ = rule.apply_rule(states, None)
        self.assertEqual(state, 0)


if __name__ == '__main__':
    unittest.main()
