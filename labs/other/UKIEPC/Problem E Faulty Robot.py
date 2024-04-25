from collections import defaultdict, deque

forced = defaultdict(set)
buggy = defaultdict(set)

n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    if a < 0:
        forced[-a].add(b)
    else:
        buggy[a].add(b)

visited = set()
endpoints = set()

queue = deque([(1, True)])

while queue:
    vertex, can_bug = queue.popleft()
    if vertex in visited:
        continue
    forced_moves = forced[vertex]
    bug_moves = buggy[vertex] - visited if can_bug else {}
    if not forced_moves:
        endpoints.add(vertex)
    for neighbour in forced_moves:
        queue.append((neighbour, can_bug))
    for neighbour in bug_moves:
        queue.append((neighbour, False))
    visited.add(vertex)

print(len(endpoints))
