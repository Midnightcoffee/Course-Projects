"""
       File : time_things.py
     Author : Drew Verlee
       Date : 04.11.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : just using timeit to time some functions
"""
from timeit import repeat
from copy import deepcopy
from tools import copy_graph, file_to_graph
from topological_sort import dfs_topological_sort, source_removal_topological_sort
import cProfile
import re

def graphing():
    Graph = {x: {y for y in range(100)} for x in range(1000)}
    print('copy graph')
    print(min(repeat(
        stmt = '{0}({1})'.format(copy_graph.func_name, Graph),
        setup = 'from __main__ import {0}'.format(copy_graph.func_name),
        repeat = 100,
        number = 5)))

    print('deep copy')
    print(min(repeat(
        stmt = '{0}({1})'.format(deepcopy.func_name, Graph),
        setup = 'from __main__ import {0}'.format(deepcopy.func_name),
        repeat = 100,
        number = 5)))

graph,_ = file_to_graph('graph30000.txt')

cProfile.run('dfs_topological_sort(graph)')
cProfile.run('source_removal_topological_sort(graph)')



