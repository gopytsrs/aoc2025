from heapq import heappush, heappop
from operator import mul
from functools import reduce
from collections import defaultdict

def parse():
    with open("data.in") as f:
        return [list(map(int, line.split(","))) for line in f]

def get_dist(node1, node2):
    dist = 0
    for p1, p2 in zip(node1, node2):
        dist += (p2 - p1) ** 2
    return dist

class UF:
    def __init__(self, n):
        self.parent = {x:x for x in range(n)}
        self.rank = {x:1 for x in range(n)}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = self.parent[py]
            self.rank[py] += self.rank[px]
        else:
            self.parent[py] = self.parent[px]
            self.rank[px] += self.rank[py]
        return True

def solve1():
    nodes = parse()
    n = len(nodes)

    closest_edges = []

    for i in range(n):
        for j in range(i+1, n):
            dist = get_dist(nodes[i], nodes[j])
            heappush(closest_edges, (-dist, i, j))
            if len(closest_edges) > 1000:
                heappop(closest_edges)

    uf = UF(n)
    while closest_edges:
        _, i, j = heappop(closest_edges)
        uf.union(i, j)

    group_sizes = defaultdict(int)
    for node in range(n):
        root = uf.find(node)
        group_sizes[root] += 1
        

    top3 = sorted(group_sizes.values(), reverse=True)[:3]
    return reduce(mul, top3, 1)

def solve2():
    nodes = parse()
    n = len(nodes)

    edges = []
    for i in range(n):
        for j in range(i+1, n):
            dist = get_dist(nodes[i], nodes[j])
            heappush(edges, (dist, i, j))

    uf = UF(n)
    components = n

    while edges:
        _, i, j = heappop(edges)

        if uf.union(i, j):
            components -= 1

            if components == 1:
                return nodes[i][0] * nodes[j][0]

print(f"Part 1: {solve1()}")
print(f"Part 2: {solve2()}")