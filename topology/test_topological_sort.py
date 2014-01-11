"""
       File : test_topological_sort.py
     Author : Drew Verlee
       Date : 16.10.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : test cases for the topogogical_sort sort
"""
import unittest
from topological_sort import dfs_topological_sort, source_removal_topological_sort


class TestDFSTopologicalSort(unittest.TestCase):
    """remember were only testing DAGS"""


    def test_basic(self):
        graph = {
                1: {2},
                2: {3},
                3: set(),
                }
        expected = [1, 2, 3]
        returned = dfs_topological_sort(graph)
        self.assertListEqual(expected, returned)


    def test_basic_two_paths(self):
        graph = {
                1: {3},
                2: {3},
                3: set()
                }
        expected = [[2, 1, 3], [1, 2, 3]]
        returned = dfs_topological_sort(graph)
        self.assertIn(returned, expected)


    def test_small_two_paths(self):
        graph = {
                1: {2},
                2: {3, 4},
                3: {5},
                4: set(),
                5: set()
                }
        expected = [[1, 2, 3, 5, 4], [1, 2, 4, 3, 5], [1, 2, 3, 4, 5]]
        returned = dfs_topological_sort(graph)
        self.assertIn(returned, expected)


    def test_small_two_paths_cross_edge(self):
        graph = {
                1: {2},
                2: {3, 4},
                3: {4, 5},
                4: set(),
                5: set()
                }
        expected = [[1, 2, 3, 5, 4], [1, 2, 3, 4, 5]]
        returned = dfs_topological_sort(graph)
        self.assertIn(returned, expected)

    def test_medium(self):
        graph = {
                1: {2, 3, 4},
                2: {3, 5},
                3: {5, 6 ,7},
                4: {3},
                5: {6},
                6: {7},
                7: set()
                }
        expected = [[1, 2, 4, 3, 5, 6, 7], [1, 4, 2, 3, 5, 6, 7]]
        returned = dfs_topological_sort(graph)
        self.assertIn(returned, expected)


class TestTestSourceRemovalTopologicalSort(unittest.TestCase):
    """topogogical_sort via source removal"""

    def test_basic(self):
        graph = {
                1: {2},
                2: {3},
                3: set(),
                }
        expected = [1, 2, 3]
        returned = source_removal_topological_sort(graph)
        self.assertListEqual(expected, returned)


    def test_basic_two_paths(self):
        graph = {
                1: {3},
                2: {3},
                3: set()
                }
        expected = [[2, 1, 3], [1, 2, 3]]
        returned = source_removal_topological_sort(graph)
        self.assertIn(returned, expected)


    def test_small_two_paths(self):
        graph = {
                1: {2},
                2: {3, 4},
                3: {5},
                4: set(),
                5: set()
                }
        expected = [[1, 2, 3, 5, 4], [1, 2, 4, 3, 5], [1, 2, 3, 4, 5]]
        returned = source_removal_topological_sort(graph)
        self.assertIn(returned, expected)


    def test_small_two_paths_cross_edge(self):
        graph = {
                1: {2},
                2: {3, 4},
                3: {4, 5},
                4: set(),
                5: set()
                }
        expected = [[1, 2, 3, 5, 4], [1, 2, 3, 4, 5]]
        returned = source_removal_topological_sort(graph)
        self.assertIn(returned, expected)


    def test_medium(self):
        graph = {
                1: {2, 3, 4},
                2: {3, 5},
                3: {5, 6 ,7},
                4: {3},
                5: {6},
                6: {7},
                7: set()
                }
        expected = [[1, 2, 4, 3, 5, 6, 7], [1, 4, 2, 3, 5, 6, 7]]
        returned = source_removal_topological_sort(graph)
        self.assertIn(returned, expected)

if __name__ == '__main__':
    unittest.main()





