"""
En este script se testea las reglas implementadas para los casos
bidimensionales
"""
import unittest

import numpy as np

from pycellslib.twodimensional.neighborhoods import MooreNeighborhood
from pycellslib.twodimensional.rules import BSNotationRule


class TestBSNotationRule(unittest.TestCase):
    """
    Tests para la clase BSNotationRule
    """

    def test_get_neighborhood(self):
        """
        Este metodo testea el metodo get_neighborhood
        """
        rule = BSNotationRule(B=[3], S=[2, 3], radius=1)
        neighborhood = rule.get_neighborhood()

        self.assertIsInstance(neighborhood, MooreNeighborhood)
        # la vecindad debe ser inclusiva
        mask = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=bool)
        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_apply_rule_case_1(self):
        """
        Este metodo testea el metodo apply_rule en el caso de tener el juego
        de la vida
        """
        rule = BSNotationRule(B=[3], S=[2, 3], radius=1)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 1, 1, 1, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 1, 1, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 1, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 0, 1, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        # muerto
        neighborhoods = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        # vivo
        neighborhoods = np.array([1, 1, 0, 0, 1, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        # muerto
        neighborhoods = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 0, 0, 0, 1, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 0, 0, 0, 0, 0, 1, 0, 1], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        # vivo
        neighborhoods = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

    def test_apply_rule_case_2(self):
        """
        Este metodo testea el metodo apply_rule
        """
        rule = BSNotationRule(B=[0], S=[2, 3], radius=1)

        neighborhoods = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        neighborhoods = np.array([1, 0, 0, 0, 0, 0, 1, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

    def test_apply_rule_case_3(self):
        """
        Este metodo testea el metodo apply_rule
        """
        rule = BSNotationRule(B=[2, 4], S=[0], radius=2)

        neighborhoods = np.array(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            dtype=int,
        )
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        neighborhoods = np.array(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            dtype=int,
        )
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            dtype=int,
        )
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        neighborhoods = np.array(
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            dtype=int,
        )
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array(
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            dtype=int,
        )
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

    def test_apply_rule_case_4(self):
        """
        Este metodo testea el metodo apply_rule
        """
        rule = BSNotationRule(B=[2], S=[], radius=1)

        neighborhoods = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array([0, 1, 0, 0, 0, 0, 1, 1, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array([0, 1, 0, 0, 1, 0, 1, 1, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array([0, 1, 0, 0, 0, 0, 0, 1, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

    def test_apply_rule_case_5(self):
        """
        Este metodo testea el metodo apply_rule
        """
        rule = BSNotationRule(B=[], S=[2], radius=1)

        neighborhoods = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        neighborhoods = np.array([1, 0, 0, 0, 0, 0, 1, 1, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        neighborhoods = np.array([0, 0, 0, 1, 0, 0, 0, 1, 1], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        neighborhoods = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array([0, 1, 0, 0, 1, 0, 1, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        neighborhoods = np.array([0, 0, 0, 0, 1, 0, 1, 0, 0], dtype=int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)
