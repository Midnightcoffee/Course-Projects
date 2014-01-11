"""
       File : tools.py
     Author : Drew Verlee
       Date : 28.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : tests for tools used in dijkstra algorithm
"""

import unittest
from dijkstra_project.main.tools import file_to_graph

class TestFileToGraph(unittest.TestCase):
    """file first column is row, then neighbor node, distance
    1 2 10,3 4... etc.."""


    def test_small_example(self):
        file_name = '../data/small.txt'
        expected = {
            1: {2: 5, 3: 1},
            2: {1: 5, 4: 10},
            3: {1: 1, 4: 1},
            4: {2: 10, 3: 1}
            }
        result = file_to_graph(file_name)
        self.assertDictEqual(expected, result)

    def test_directed_example(self):
        file_name = '../data/medium.txt'
        expected = {
            1: {2: 2, 4: 1},
            2: {4: 3, 5: 10},
            3: {1: 4, 6: 5},
            4: {3: 2, 5:2, 6:8, 7:4},
            5: {7: 6},
            7: {6: 1}
            }
        result = file_to_graph(file_name)
        self.assertDictEqual(expected, result)
    
if __name__ == '__main__':
    unittest.main()

