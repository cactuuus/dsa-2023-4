import math
from collections import defaultdict

while True:
    # reads graph data, breaks if "0 0 0 0" is fed
    nodes, edges, queries, curr_node = [int(x) for x in input().split(" ")]
    if nodes == 0:
        break

    # store edges (paths) in a dictionary
    paths = defaultdict(list)
    for _ in range(edges):
        start, to, weight = [int(x) for x in input().split(" ")]
        paths[start].append((to, weight))

    # track the shortest paths and visited nodes
    distances = {curr_node: 0}
    visited = set()
    while curr_node is not None:
        for to, weight in paths.get(curr_node, []):
            tot_weight = distances[curr_node] + weight
            if tot_weight < distances.get(to, math.inf):
                distances[to] = tot_weight
        visited.add(curr_node)
        curr_node = min(visited ^ distances.keys()) if visited ^ distances.keys() else None

    # handles queries
    for _ in range(queries):
        print(distances.get(int(input()), "Impossible"))
