"""
En este script se testean las vecindades definidas para los casos
unidimensionales
"""

import unittest

import numpy as np

from pycellslib.twodimensional.neighborhoods import (
    MooreNeighborhood,
    NeumannNeighborhood,
)


class TestMooreNeighborhood(unittest.TestCase):
    """
    Test para la clase MooreNeigborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask con radio 1
        """
        neighborhood = MooreNeighborhood(1, inclusive=False)
        mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask con radio 4
        """
        neighborhood = MooreNeighborhood(4, inclusive=True)
        mask = np.ones((9, 9), dtype=bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_offset con radio 1
        """
        neighborhood = MooreNeighborhood(1)
        offset = (-1, -1)

        self.assertEqual(neighborhood.get_offset(), offset)

    def test_get_offset_case_2(self):
        """
        Este metodo testea el metodo get_offset con radio 4
        """
        neighborhood = MooreNeighborhood(4)
        offset = (-4, -4)

        self.assertEqual(neighborhood.get_offset(), offset)


class TestCircularNeighborhood(unittest.TestCase):
    """
    Test para la clase CircularNeighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask con radio 1
        """

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask con radio 4
        """

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_offset con radio 1
        """

    def test_get_offset_case_2(self):
        """
        Este metodo testea el metodo get_offset con radio 4
        """


class TestL2Neighborhood(unittest.TestCase):
    """
    Test para la clase L2Neighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask con radio 1
        """

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask con radio 4
        """

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_offset con radio 1
        """

    def test_get_offset_case_2(self):
        """
        Este metodo testea el metodo get_offset con radio 4
        """


class TestNeumannNeighborhood(unittest.TestCase):
    """
    Test para la clase NeumannNeighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask con radio 1
        """
        neighborhood = NeumannNeighborhood(1, inclusive=False)
        mask = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask con radio 4
        """
        neighborhood = NeumannNeighborhood(2, inclusive=True)
        mask = np.array(
            [
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
            ],
            dtype=bool,
        )

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_3(self):
        """
        Este metodo testea el metodo get_mask con radio 4
        """
        neighborhood = NeumannNeighborhood(4, inclusive=False)
        mask = np.array(
            [
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
            ],
            dtype=bool,
        )

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_offset con radio 1
        """
        neighborhood = NeumannNeighborhood(1)
        offset = (-1, -1)

        self.assertEqual(neighborhood.get_offset(), offset)

    def test_get_offset_case_2(self):
        """
        Este metodo testea el metodo get_offset con radio 4
        """
        neighborhood = NeumannNeighborhood(4)
        offset = (-4, -4)

        self.assertEqual(neighborhood.get_offset(), offset)
