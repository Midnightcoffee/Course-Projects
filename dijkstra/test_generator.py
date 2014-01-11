"""
       File : test_generator.py
     Author : Drew Verlee
       Date : 28.07.13.
     GitHub : https://github.com/Midnightcoffee/
Description : creates a random graph file
"""

import networkx as nx
from random import randrange as rr
import pylab

def random_weighted_graph(size):
    """Creates random graph

    :size: int: number of nodes in graph
    :returns: nx.Graph object

    """
    nodes = size
    edges = nodes* (nodes/3)
    MAX_WEIGHT = 100
    G = nx.dense_gnm_random_graph(n=nodes, m=edges)
    # give our graph some random weights
    for edge in G.edges(): G.add_edge(*edge, weight = rr(MAX_WEIGHT))
    assert nx.is_connected(G) == True # make sure its connected
    return G

def graph_to_file(G, file_name="graph"):
    """creates random graph

    :G: networkx Graph object
    :creates: a graph file

    """

    graph_file = open(file_name, 'w')
    for node in G:
        graph_file.write(str(node))
        for neighbor in G[node]:
            graph_file.write(' ' +','.join(
                (str(neighbor),str(G[node][neighbor]['weight']))))
        graph_file.write('\n')
    graph_file.close()

def visulizer(G, i=0):
    """creates a visual aid

    :G: nx object
    :creates: file object

    """
    pos=nx.spring_layout(G)
    pylab.figure(2)
    nx.draw(G,pos)
    edge_labels=dict([((u,v,),d['weight'])
                for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    pylab.savefig('graphs/graph{0}'
            .format(i).replace('txt','png'))

def run():
    """ generates some files, graphs and store there results in graphs/result"""
    import os
    from random import choice
    from tools import file_to_graph #FIXME change me to use your algorithm
    # from dijkstra import dijkstra #FIXME change me to use your algorithm
    import shutil
    def FAIL(G,v,f): return None #FIXME remove
    dijkstra = FAIL             #FIXME remove
    file_to_graph = file_to_graph #FIXME so its dijkstra = your algorithm
    print('number of tests?'),
    num_tests = input()
    print('graph size ? '),
    size = input()
    test_index = 0
    folder = 'graphs'
    if os.path.exists(folder):
        shutil.rmtree('graphs/') # note we delete the folder everytime
    if not os.path.exists(folder):
        os.makedirs(folder)
    for x in xrange(num_tests):
        test_file = 'graphs/graph' + str(test_index) + '.txt'
        G = random_weighted_graph(size)
        graph_to_file(G, test_file)
        start =  choice(G.nodes())
        finish = choice(G.nodes())
        while start == finish: finish = choice(G.nodes())
        cost = nx.dijkstra_path_length(G, start, finish)
        NG = file_to_graph(test_file)
        if dijkstra(NG, start, finish) != cost:
            path = nx.dijkstra_path(G, start, finish)
            visulizer(G,test_index)
            result = 'Graph{0} failed to find lowest cost {1} with path {2} with start point {3} and finish {4}\n'.\
                format(test_index, cost, path, start, finish)
        else:
            result = 'Graph{0} passed!\n'
        with open('graphs/results.txt', 'a') as results:
            results.write(result)
        test_index += 1

if __name__ == '__main__':
    run()

