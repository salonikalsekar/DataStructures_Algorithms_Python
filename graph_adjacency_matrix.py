

class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.vertices:
            self.vertices[v.name]= v
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[v.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edges(self, u,v, weight = 1 ):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True

        else:
            return False

    def print_graph(self):

        for i, j in sorted(self.edge_indices.items()):
            print(i, end=" ")
            for edge in self.edges[j]:
                print(edge, end=" ")
            print()


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))
print(len(g.vertices))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edges(edge[:1], edge[1:])

g.print_graph()