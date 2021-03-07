from data_structures.graphs_ds.priority_queue import PriorityQueue
from data_structures.graphs_ds.graph_adt import Graph, Vertex
import sys


def prim_algo(a_graph, start):
    pq = PriorityQueue()
    for vertex in a_graph:
        vertex.set_distance(sys.maxsize)
        vertex.set_predecessor(None)
    start.set_distance(0)
    pq.build_heap([(vertex.get_distance(), vertex) for vertex in a_graph])
    while not pq.is_empty():
        current_vertex = pq.del_min()
        for next_vertex in current_vertex.get_connections():
            new_weight = current_vertex.get_weight(next_vertex) + \
                         current_vertex.get_distance()
            if vertex in pq and new_weight < next_vertex.get_distance():
                next_vertex.set_predecessor(current_vertex)
                next_vertex.set_distance(new_weight)
                pq.decrease_key(next_vertex, new_weight)
