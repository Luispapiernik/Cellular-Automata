import numpy as np

from pycellslib import Rule
from pycellslib.twodimensional.neighborhoods import MooreNeighborhood


class BSNotationRule(Rule):
    """
    Esta clase representa las reglas de transicion denotadas con la notacion
    B/S Notation
    """

    def test_get_neighborhood(self):
        """
        Este metodo testea el metodo get_neighborhood
        """
        rule = BSNotationRule(B=[3], S=[2, 3], radius=1)
        neighborhood = rule.get_neighborhood()

        self.assertIsInstance(neighborhood, MooreNeighborhood)
        # la vecindad debe ser inclusiva
        mask = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.bool)
        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_apply_rule(self):
        """
        Este metodo testea el metodo apply_rule en el caso de tener el juego
        de la vida
        """
        rule = BSNotationRule(B=[3], S=[2, 3], radius=1)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)


        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 1, 1, 1, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 1, 1, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 1, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        neighborhoods = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 1, 1, 0, 1, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        # muerto
        neighborhoods = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        # vivo
        neighborhoods = np.array([1, 1, 0, 0, 1, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([1, 0, 0, 0, 1, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # vivo
        neighborhoods = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 0)

        # muerto
        neighborhoods = np.array([1, 0, 0, 0, 0, 0, 1, 0, 1], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)

        # vivo
        neighborhoods = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1], dtype=np.int)
        state, _ = rule.apply_rule(neighborhoods, None)
        self.assertEqual(state, 1)
