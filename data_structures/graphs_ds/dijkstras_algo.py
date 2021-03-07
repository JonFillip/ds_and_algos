from data_structures.graphs_ds.graph_adt import Graph, Vertex
from data_structures.graphs_ds.priority_queue import PriorityQueue
import unittest


def dijkstras_algo(graph_sample, start):
    pq = PriorityQueue()
    start.set_distance()
    pq.build_heap([(vertex.get_distance(), vertex) for vertex in graph_sample])
    while not pq.is_empty():
        current_vertex = pq.del_min()
        for next_vertex in current_vertex.get_connections():
            new_distance = current_vertex.get_distance() + \
                           current_vertex.get_weight(next_vertex)

            if new_distance < next_vertex.get_distance():
                next_vertex.set_distance(new_distance)
                next_vertex.set_predecessor(current_vertex)
                pq.decrease_key(next_vertex, new_distance)


class DijkstrasTest(unittest.TestCase):
    """Test dijkstras algorithm"""

    def setUp(self):
        self.heap_list = [
            (2, 'Bowl'),
            (3, 'Eggs'),
            (1, 'flour'),
            (4, 'Mix'),
            (6, 'Fry'),
            (8, 'serve')
        ]
        self.test_graph = Vertex(0)

        for vertex in self.heap_list:
            self.test_graph.id = vertex[1]
            self.test_graph = Vertex(vertex[1])
        for edge, vertex in self.heap_list:
            self.test_graph.add_neighbour(vertex[1], edge[0])

    def test_algo(self):
        dijkstras_algo(self.test_graph, self.test_graph.id[0])
