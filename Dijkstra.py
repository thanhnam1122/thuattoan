import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            cost, u = heapq.heappop(pq)

            if cost > dist[u]:
                continue

            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        print("Dinh\tKhoang cach tu nguon")
        for i in range(self.V):
            print(f"{i}\t{dist[i]}")

g = Graph(5)
g.add_edge(0, 1, 9)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(0, 4, 3)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 4)
g.dijkstra(0)