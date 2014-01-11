"""
       File : test_dijkstra.py
     Author : Drew Verlee
       Date : 28.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : test dijkstra to find shortest cost path
"""
import unittest
from dijkstra import dijkstra
from tools import file_to_graph

class TestDijkstra(unittest.TestCase):
    """Test case docstring"""

    file_path = 'data/'

    def test_small_example(self):
        file_name = self.file_path + 'small.txt'
        start, finish = 1, 4
        expected = 2
        G = file_to_graph(file_name)
        final_dist = dijkstra(G,start)
        result = final_dist[finish]
        self.assertEqual(expected, result)

    def test_medium_example(self):
        file_name = self.file_path + 'medium.txt'
        start, finish = 1,7
        expected = 5
        G = file_to_graph(file_name)
        final_dist = dijkstra(G,start)
        result = final_dist[finish]
        self.assertEqual(expected, result)

    def test_large_example(self):
        file_name = self.file_path + 'large.txt'
        start, finish = 13,5
        expected = 26
        G = file_to_graph(file_name)
        final_dist = dijkstra(G,start)
        result = final_dist[finish]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
