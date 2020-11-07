"""
En este script se testean las vecindades definidas para los casos
unidimensionales
"""

import unittest

import numpy as np

from pycellslib.onedimensional.neighborhoods import LeftCellNeighborhood
from pycellslib.onedimensional.neighborhoods import RightCellNeighborhood
from pycellslib.onedimensional.neighborhoods import IntervalCellNeighborhood
from pycellslib.onedimensional.neighborhoods import LeftSideNeighborhood
from pycellslib.onedimensional.neighborhoods import RightSideNeighborhood
from pycellslib.onedimensional.neighborhoods import BothSideNeighborhood


class TestLeftCellNeighborhood(unittest.TestCase):
    """
    Tests para LeftCellNeighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase LeftCellNeighborhood
        """
        neighborhood = LeftCellNeighborhood(4, inclusive=False)
        # son 5 entradas en el array porque se cuenta a la celula como un
        # vecino
        mask = np.array([[1, 0, 0, 0, 0]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase LeftCellNeighborhood
        """
        neighborhood = LeftCellNeighborhood(3, inclusive=True)
        mask = np.array([[1, 0, 0, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase LeftCellNeighborhood
        """
        neighborhood = LeftCellNeighborhood(4)
        offset = (0, -4)

        self.assertEqual(neighborhood.get_offset(), offset)

    def test_get_offset_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase LeftCellNeighborhood
        """
        neighborhood = LeftCellNeighborhood(3)
        offset = (0, -3)

        self.assertEqual(neighborhood.get_offset(), offset)


class TestRightCellNeighborhood(unittest.TestCase):
    """
    Tests para RightCellNeighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase RightCellNeighborhood
        """
        neighborhood = RightCellNeighborhood(4, inclusive=False)
        # son 5 entradas en el array porque se cuenta a la celula como un
        # vecino
        mask = np.array([[0, 0, 0, 0, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase RightCellNeighborhood
        """
        neighborhood = RightCellNeighborhood(3, inclusive=True)
        mask = np.array([[1, 0, 0, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase RightCellNeighborhood
        """
        neighborhood = RightCellNeighborhood(4)
        offset = (0, 0)

        self.assertEqual(neighborhood.get_offset(), offset)


class TestIntervalCellNeighborhood(unittest.TestCase):
    """
    Tests para IntervalCellNeighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase
        IntervalCellNeighborhood
        """
        neighborhood = IntervalCellNeighborhood(4, 3, inclusive=False)
        # son 5 entradas en el array porque se cuenta a la celula como un
        # vecino
        mask = np.array([[1, 0, 0, 0, 0, 0, 0, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase
        IntervalCellNeighborhood
        """
        neighborhood = IntervalCellNeighborhood(3, 4, inclusive=True)
        mask = np.array([[1, 0, 0, 1, 0, 0, 0, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase
        IntervalCellNeighborhood
        """
        neighborhood = IntervalCellNeighborhood(4, 3)
        offset = (0, -4)

        self.assertEqual(neighborhood.get_offset(), offset)

    def test_get_offset_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase
        IntervalCellNeighborhood
        """
        neighborhood = IntervalCellNeighborhood(3, 4)
        offset = (0, -3)

        self.assertEqual(neighborhood.get_offset(), offset)


class TestLeftSideNeighborhood(unittest.TestCase):
    """
    Tests para LeftSideNeighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase
        LeftSideNeighborhood
        """
        neighborhood = LeftSideNeighborhood(4, inclusive=False)
        # son 5 entradas en el array porque se cuenta a la celula como un
        # vecino
        mask = np.array([[1, 1, 1, 1, 0]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase
        LeftSideNeighborhood
        """
        neighborhood = LeftSideNeighborhood(3, inclusive=True)
        mask = np.array([[1, 1, 1, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase
        LeftSideNeighborhood
        """
        neighborhood = LeftSideNeighborhood(4)
        offset = (0, -4)

        self.assertEqual(neighborhood.get_offset(), offset)

    def test_get_offset_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase
        LeftSideNeighborhood
        """
        neighborhood = LeftSideNeighborhood(3)
        offset = (0, -3)

        self.assertEqual(neighborhood.get_offset(), offset)


class TestRightSideNeighborhood(unittest.TestCase):
    """
    Tests para RightSideNeighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase RightSideNeighborhood
        """
        neighborhood = RightSideNeighborhood(4, inclusive=False)
        # son 5 entradas en el array porque se cuenta a la celula como un
        # vecino
        mask = np.array([[0, 1, 1, 1, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase RightSideNeighborhood
        """
        neighborhood = RightSideNeighborhood(3, inclusive=True)
        mask = np.array([[1, 1, 1, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase RightSideNeighborhood
        """
        neighborhood = RightSideNeighborhood(4)
        offset = (0, 0)

        self.assertEqual(neighborhood.get_offset(), offset)

class TestBothSideNeighborhood(unittest.TestCase):
    """
    Tests para BothSideNeighborhood
    """

    def test_get_mask_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase
        BothSideNeighborhood
        """
        neighborhood = BothSideNeighborhood(4, 3, inclusive=False)
        # son 5 entradas en el array porque se cuenta a la celula como un
        # vecino
        mask = np.array([[1, 1, 1, 1, 0, 1, 1, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_mask_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase
        BothSideNeighborhood
        """
        neighborhood = BothSideNeighborhood(3, 4, inclusive=True)
        mask = np.array([[1, 1, 1, 1, 1, 1, 1, 1]], dtype=np.bool)

        self.assertTrue(np.array_equal(neighborhood.get_mask(), mask))

    def test_get_offset_case_1(self):
        """
        Este metodo testea el metodo get_mask de la clase
        BothSideNeighborhood
        """
        neighborhood = BothSideNeighborhood(4, 3)
        offset = (0, -4)

        self.assertEqual(neighborhood.get_offset(), offset)

    def test_get_offset_case_2(self):
        """
        Este metodo testea el metodo get_mask de la clase
        BothSideNeighborhood
        """
        neighborhood = BothSideNeighborhood(3, 4)
        offset = (0, -3)

        self.assertEqual(neighborhood.get_offset(), offset)

if __name__ == '__main__':
    unittest.main()
