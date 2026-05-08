class UnionFind:
    def __init__(self, vertices):
        # parent and rank dictionaries
        self.parent = {}
        self.rank = {}

        # initially every vertex is its own parent
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, x):
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        # already in same set
        if px == py:
            return False

        # union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True


def kruskal(edges):
    # collect all vertices
    vertices = set()

    for u, v, w in edges:
        vertices.add(u)
        vertices.add(v)

    # create UnionFind
    uf = UnionFind(vertices)

    # sort edges by weight
    edges.sort(key=lambda x: x[2])

    cost = 0
    mst = []

    # process edges
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w

    return mst, cost


# INPUT EDGES (Alphabet vertices)
edges = [
    ('A', 'B', 10),
    ('A', 'C', 6),
    ('A', 'D', 5),
    ('B', 'D', 15),
    ('C', 'D', 4)
]

# Run Kruskal
mst, cost = kruskal(edges)

# Output
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total Cost:", cost)

