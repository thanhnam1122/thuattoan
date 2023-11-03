class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[float("inf")] * vertices for _ in range(vertices)]
        for i in range(vertices):
            self.graph[i][i] = 0

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def floyd_warshall(self):
        dist = self.graph

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        print("Khoang cach ngan nhat cua moi cap dinh:")
        for i in range(self.V):
            for j in range(self.V):
                if dist[i][j] == float("inf"):
                    print("INF", end="\t")
                else:
                    print(dist[i][j], end="\t")
            print()

g = Graph(4)
g.add_edge(0, 1, 3)
g.add_edge(0, 3, 7)
g.add_edge(1, 0, 2)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 1)
g.add_edge(3, 2, 2)
g.floyd_warshall()
