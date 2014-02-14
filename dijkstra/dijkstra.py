"""
       File : dijkstra.py
     Author : Drew Verlee
       Date : 28.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : dijkstra's algorithm finds the shortest path, useful for a 
weighted graph source: https://www.udacity.com/wiki/cs215/unit5solutions-1.
"""

import heapq
from collections import defaultdict
from tools import file_to_graph


def val(pair): return pair[0]
def id(pair): return pair[1]

def dijkstra(G,v, finish=None):
    """
    A graph search algorithm that solves the single-source shortest path 
    problem for a graph with non-negative edge path costs, producing a 
    shortest path tree.
    """
    heap = [ [0, v] ]
    dist_so_far = {v:[0, v]}
    final_dist = {}
    while len(final_dist) < len(G):
        # find the closest un-explored node
        while True:
            w = heapq.heappop(heap)
            # grab the relevant parts of w
            node = id(w)
            dist = val(w)
            if node != 'REMOVED':
                del dist_so_far[node]
                break
        #Lock it down!
        final_dist[node] = dist
        # look at its neighbors
        for x in G[node]:
            # but only those that haven't been locked down
            if x not in final_dist:
                new_dist = dist + G[node][x]
                new_entry = [new_dist, x]
                if x not in dist_so_far:
                    # we haven't see this yet
                    # so add to the heap and the dictionary
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
                elif new_dist < val(dist_so_far[x]):
                    # the new distance is less then the 
                    # best known
                    # Instead of removing it from the heap
                    # which could be expensive, mark it
                    dist_so_far[x][1] = "REMOVED"
                    # and then add a new entry
                    # for this node
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)

    if finish:
        return ','.join([str(final_dist[x]) for x in finish])
    else: return final_dist

if __name__ == '__main__':
    import sys
    # file_name, start, finish = sys.argv[1:]
    # wont work for pyc
    # from tools import  file_to_graph
    # G = file_to_graph(file_name)
    # final_dist = dijkstra(G, int(start))
    # print(final_dist[int(finish)])
    G = file_to_graph('data/dijkstraData.txt')
    print dijkstra(G, 1, finish=[7,37,59,82,99,115,133,165,188,197])


