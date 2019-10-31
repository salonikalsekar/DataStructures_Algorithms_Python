

class Vertex:

    def __init__(self, n):

        self.name = n
        self.neighbours = list()

    def add_neighbour(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()


class Graph:
    vertices = {}
    def add_vertex(self, v):

        if isinstance(v, Vertex) and v.name not in self.vertices:
            self.vertices[v.name] = v
            return True
        else:
            return False


    def add_edge(self, u, v):

        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbour(v)
            self.vertices[v].add_neighbour(u)

            return True

        else:
            return False



    def print_graph(self):

        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours))


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()
