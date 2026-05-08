
# /------ prims algorithm -------/
import heapq

def prim(graph, start):
    visited = set()

    # (weight, current_node, parent)
    min_heap = [(0, start, None)]

    mst = []
    total_cost = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        if parent is not None:
            mst.append((parent, node, weight))

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (cost, neighbor, node))

    return mst, total_cost


graph = {
    'A': [('B',2), ('C',6), ('D',3)],
    'B': [('A',2), ('D',8)],
    'C': [('A',6), ('D',5)],
    'D': [('A',3), ('B',8), ('C',5)]
}

mst, cost = prim(graph, 'A')

print("MST Edges:")
for u, v, w in mst:
    print(u, "-", v, "=", w)

print("Total Cost:", cost)



# /--- Dijkstra algorithm ----/
import heapq


def dijkstra(graph, start):
    # store shortest distance to each node
    dist = {node: float('inf') for node in graph}

    # starting node distance = 0
    dist[start] = 0

    # min heap (distance, node)
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)

        # skip outdated heap entry
        if d > dist[node]:
            continue

        # check neighbors
        for neighbor, weight in graph[node]:
            new_dist = d + weight

            # if shorter path found
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist


# Graph input
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Start node
start = 'A'

# Run algorithm
result = dijkstra(graph, start)

# Print shortest distances
print("Shortest distances from", start)

for node in result:
    print(start, "->", node, "=", result[node])





# /----job scheduling-------/
def job_scheduling(jobs):
    # jobs = (id, deadline, profit)

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline

    total_profit = 0

    for job_id, deadline, profit in jobs:
        # latest possible slot
        for j in range(deadline - 1, -1, -1):
            if slots[j] is None:
                slots[j] = job_id
                total_profit += profit
                break

    return slots, total_profit


jobs = [
    ('A', 2, 100),
    ('B', 1, 19),
    ('C', 2, 27),
    ('D', 1, 25),
    ('E', 3, 15)
]

schedule, profit = job_scheduling(jobs)

print("Schedule:", schedule)
print("Profit:", profit)