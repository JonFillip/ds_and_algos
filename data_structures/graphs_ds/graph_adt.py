class Vertex:
    """Representation of the vertices in a adjacent list graph"""

    def __init__(self, key):
        self.id = key  # Represents the vertex or main node
        self.path_to = {}  # Represents the values or weights connecting each
        # vertex

    def add_neighbour(self, new_vertex, weight=0):
        """Adds a new vertex and weight"""
        self.path_to[new_vertex] = weight

    def __str__(self):
        return f"{self.id} is connected to: {[x.id for x in self.path_to]}"

    def get_connections(self):
        """Returns the path and weights connected to a vertex"""
        return self.path_to.keys()

    def get_id(self):
        """Returns the vertex"""
        return self.id

    def get_weight(self, new_vertex):
        """Returns the weight connected to a specified vertex"""
        return self.path_to[new_vertex]

    def set_color(self):
        """Returns a color from black, gray and white to indicate nodes
        already traversed"""


class Graph:
    """Implementation of a adjacent list graph representation"""
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """Adds a new vertex to the list"""
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, node):
        """Checks to see if the searched for vertex is in the dict and
        returns it*"""
        if node in self.vertices:
            return self.vertices[node]
        else:
            return None

    def __contains__(self, node):
        """Returns a boolean value whether or not the vertex is in the list"""
        return node in self.vertices

    def add_edge(self, from_v, to_v, cost=0):
        """Adds a path connecting one vertex to another"""
        if from_v not in self.vertices:
            self.add_vertex(from_v)
        if to_v not in self.vertices:
            self.add_vertex(to_v)
        self.vertices[from_v].add_neighbour(self.vertices[to_v], cost)

    def get_vertices(self):
        """Returns a list of vertices in the dictionary"""
        return self.vertices.keys()

    def __iter__(self):
        """Iterate or traverse through the dictionary or graph value(weights)"""
        return iter(self.vertices.values())
