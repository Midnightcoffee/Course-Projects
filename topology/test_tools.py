"""
       File : test_tools.py
     Author : Drew Verlee
       Date : 17.10.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : test the various tools used for topological sorting
"""

import unittest
from tools import file_to_graph, inverse_graph, find_sources

class TestFileToGraph(unittest.TestCase):

    def test_graph7_graph(self):
        a_file = 'graph7.txt'
        expected = {
                0: {1, 2, 4},
                1: {3, 5},
                2: {3, 6},
                3: {7},
                4: {5, 6},
                5: {7},
                6: {7},
                7: set()
                }
        returned, _ = file_to_graph(a_file)
        self.assertEqual(expected, returned)

    def test_graph7_edge_count(self):
        a_file = 'graph7.txt'
        expected = 12
        _, returned, _ = file_to_graph(a_file)
        self.assertEqual(expected, returned)

class TestFileToGraph(unittest.TestCase):

    def test_graph7_graph(self):
        a_file = 'graph7.txt'
        expected = {
                0: {1, 2, 4},
                1: {3, 5},
                2: {3, 6},
                3: {7},
                4: {5, 6},
                5: {7},
                6: {7},
                7: set()
                }
        returned, _, _ = file_to_graph(a_file)
        self.assertEqual(expected, returned)

    def test_graph7_edge_count(self):
        a_file = 'graph7.txt'
        expected = 12
        _, returned = file_to_graph(a_file)
        self.assertEqual(expected, returned)

class TestInvertGraph(unittest.TestCase):
    """Go from {v : {outgoing edges}} to {v : incoming} """


    def test_basic(self):
        graph =  {
                1: {2},
                2: {3},
                3: set()
                }
        expected = {
                1: set(),
                2: {1},
                3: {2},
                }
        returned = inverse_graph(graph)
        self.assertEqual(expected, returned)

class TestFindSources(unittest.TestCase):
    """make sure we can find sources and degrees of all vertices"""


    def test_basic(self):
        graph = {
                1: set(),
                2: {1},
                3: {2},
                }
        sources = {1}
        expected = sources
        returned = find_sources(graph)
        self.assertSetEqual(expected, returned)





if __name__ == '__main__':
    unittest.main()
