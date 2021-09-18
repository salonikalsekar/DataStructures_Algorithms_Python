class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        head_arr = []
        count = size - 1
        res = 0
        uf = UnionFind(size)
        visited = [False] * size
        # for i in range(size):
        for j in range(1, size):
            point1 = points[0]
            point2 = points[j]
            cost = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
            edge = Edge(0, j, cost)

            heapq.heappush(head_arr, edge)
        visited[0] = True
        while head_arr and count > 0:
            e = heapq.heappop(head_arr)

            if not visited[e.point2]:
                visited[e.point2] = True
                res += e.cost
                for j in range(size):
                    if not visited[j]:
                        cost = abs(points[e.point2][0] - points[j][0]) + abs(points[e.point2][1] - points[j][1])
                        edge = Edge(e.point2, j, cost)
                        heapq.heappush(head_arr, edge)
                count -= 1
        return res


class Edge:
    def __init__(self, x, y, cost):
        self.point1 = x
        self.point2 = y
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


class UnionFind:
    def __init__(self, size):
        self.rank = [1] * size
        self.root = [i for i in range(size)]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def find(self, x):
        if self.root[x] == x:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def isconnected(self, x, y):
        return self.find(x) == self.find(y)
