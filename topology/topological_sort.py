"""
       File : dfs.py
     Author : Drew Verlee
       Date : 16.10.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : two topogogical_sorting algorithms. Created as
part of Wayne Unv. 3100 algorithms class homework 4.
"""
from random import choice
from copy import deepcopy
from tools import inverse_graph, find_sources, copy_graph


def dfs_topological_sort(graph):
    """
    A non-recursive depth first search for creating a topological sort
    :Graph: dict of sets: DAG {vertex (with d_edge to...): {these neighbors}}
    :returns: list: topological order of the DAG
    """
    G = copy_graph(graph)
    discovered = set()
    pop_order = []
    while G:
        vertex = next(G.iterkeys())
        stack = [vertex]
        discovered.add(vertex)
        while stack:
            vertex = stack[-1]
            if not discovered.issuperset(G[vertex]):
                neighbor = G[vertex].pop()
                if neighbor not in discovered:
                    discovered.add(neighbor)
                    stack.append(neighbor)
            else:
                temp = stack.pop()
                pop_order.append(temp)
                del G[temp]
    pop_order.reverse()
    return pop_order


def source_removal_topological_sort(graph):
    """A non-recursive topogogical_sorting algorithm using source removal
    :graph: dict with key as vertex and value as INCOMING edges
    :returns: list of ints: a topological order
    """
    IG = inverse_graph(graph)
    sources = find_sources(IG)
    remove_order = []
    while sources:
        source = sources.pop()
        remove_order.append(source)
        for neighbor in graph[source]:
            IG[neighbor].remove(source)
            if len(IG[neighbor]) == 0:
                sources.add(neighbor)
    return remove_order
