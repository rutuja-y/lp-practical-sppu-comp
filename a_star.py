def astar(graph, start, goal, h):
    open_list = [start]
    closed_list = []

    g = {start: 0}
    parent = {start: None}

    while open_list:
        # choose node with lowest f = g + h
        n = open_list[0]
        for i in open_list:
            if g[i] + h[i] < g[n] + h[n]:
                n = i

        # goal reached
        if n == goal:
            path = []
            while n:
                path.append(n)
                n = parent[n]
            return path[::-1]

        open_list.remove(n)
        closed_list.append(n)

        # check neighbors
        for (m, cost) in graph[n]:
            if m not in open_list and m not in closed_list:
                open_list.append(m)
                parent[m] = n
                g[m] = g[n] + cost
            else:
                if g[m] > g[n] + cost:
                    g[m] = g[n] + cost
                    parent[m] = n

    return None


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic
h = {
    'A': 6, 'B': 4, 'C': 4,
    'D': 2, 'E': 1, 'F': 0
}

# Run
print(astar(graph, 'A', 'F', h))