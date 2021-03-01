from data_structures.graphs_ds.graph_adt import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.set_color('white')  # Vertices that have not been
            # traversed are colored white
            vertex.set_predecessor(-1)
        for vertex in self:
            if vertex.get_color() == 'white':
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == "white":
                next_vertex.set_predecessor(start_vertex)
                self.dfs_visit(next_vertex)
        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish(self.time)
