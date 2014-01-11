"""
       File : tools.py
     Author : Drew Verlee
       Date : 17.10.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : tools for file manipulation and anything else
"""
from timeit import repeat
from collections import defaultdict as dd
import matplotlib.pyplot  as plt

def file_to_graph(a_file):
    """converts a file into a graph

    :a_file: str: file's name
    :returns: Graph: dict of sets {vertex: with outgoing edges to {neighbors}}

    """
    graph = dict()
    edge_count = 0
    vertices = set()
    with open(a_file) as f:
        for line in f.readlines():
            v1, v2 = map(int, line.split())
            vertices.add(v1)
            vertices.add(v2)
            if not v1 in graph:
                graph[v1] = set([v2])
                edge_count +=1
            else:
                graph[v1].add(v2)
                edge_count +=1
            if not v2 in graph:
                graph[v2] = set()
    return graph, edge_count, len(vertices)


def run_time_anyalsis(function, function_input, num, rep, analysys=min):
    """using timeit module collects information about run time of a function

    :function: function: for topological_sort
    :function_input: string: input to function
    :number: int: num of times to run function, gives results graphed on that number
    :analysis: function: for instance the min of the function gives the fastest
    run. Which is probable the only number were interested in as other
    variations in speed are caused by processor.

    :returns: list of floats: run times

    """
    return analysys(repeat(
            stmt="{0}({1})".format(function.func_name, function_input),
            setup="from __main__ import {0}".format(function.func_name),
            repeat=rep,
            number=num))


def line_plot_compare(packages, plot_name, xlabel, ylabel):
    """compares data from multiple packages and creates a graph

    : packages/tuple(...
        package/tuple(
            function_name/str,
            edge_count/list of ints,
            run_times_seconds/list of ints)
            plot_type/str
        )
    )
    :plot_name: str
    : xlable: string
    : ylable: string
    :create png. file with plot_name

    """
    for package in packages:
        function_name, edge_count, run_times_seconds, plot_type = package
        plt.plot(edge_count, run_times_seconds, plot_type)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(plot_name)
    # fig = plt.figure(figsize=(10,10), dpi=100)
    plt.savefig(plot_name)



def inverse_graph(graph):
    """Go from {v : {outgoing edges}} to {v : incoming} 

    :graph: dict with key as int/vertex and value as OUTGOING edges
    :returns: :graph: dict with key as int/vertex as INCOMING edges

    """
    inverse_graph = dd(set)
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            inverse_graph[neighbor].add(vertex)
            inverse_graph[vertex]
    return inverse_graph


def find_sources(graph):
    """find sources i.e vertices with in-degree 0

    :graph: key=vertice/int, value = set of ints/neighbors
    :returns: set of ints/sources

    """
    return {vertex for vertex, neighbors in graph.items() if len(neighbors) == 0}


def make_dag(size, file_name):
    """creates a dag

    :size:
    :creates a file that implies
        vertex directed edge to vertex
    so then...
        v v
        v v
        ...
    :file_name: str: title of file

    """
    # TODO make this function
    pass

def write_results(edges, dfs, sr, name):
    """
    just as it says it write the results to a file
    """
    afile = open(name, 'w')
    afile.close()
    with open(name, 'a') as myfile:
        myfile.write('{0:10} | {1:20} | {2:20}\n'.format('edge count', 'depth first search', 'source removal'))
        for i in range(len(edges)):
            myfile.write('{0:10} | {1:20} | {2:20}\n'.format(edges[i], dfs[i], sr[i]))


def copy_graph(graph):
    """

    :graph: dict of set
    :returns: dict of set

    """
    return {key: value for key,value in graph.items()}

