from data_structures.graphs_ds.graph_adt import Graph, Vertex
from data_structures.queues_ds.queue import Queue


def breath_first_search(graph, start):
    """BFS traverses the nodes/vertices of the graph. The function takes in
    two parameters; graph - holds the graph ADT and start - the source
    node/vertex in which the algorithm starts traversing from."""
    start.set_distance(0)
    start.set_predecessor(None)
    vertex_queue = Queue()
    vertex_queue.enqueue(start)
    while vertex_queue.size() > 0:
        current_vertex = vertex_queue.dequeue()
        for new_vertex in current_vertex.get_connections():
            if new_vertex.get_color() == "white":
                new_vertex.set_color('gray')
                new_vertex.set_distance(current_vertex.get_distance() + 1)
                new_vertex.set_predecessor(current_vertex)
                vertex_queue.enqueue(new_vertex)
        current_vertex.set_color('black')


def traverse(y):
    x = y
    while (x.get_connection()):
        print(x.get_id())
        x = x.get_connections()
    print(x.get_id())


graph = Graph()
graph.add_vertex("Man")
graph.add_vertex("Dan")
graph.add_vertex("Tan")
graph.add_vertex("Ran")
graph.add_vertex("Men")

breath_first_search(graph, graph.vertices[0])
