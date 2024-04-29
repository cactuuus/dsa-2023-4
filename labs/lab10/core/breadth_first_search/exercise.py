from typing import Optional
from lib.type_vars import VertexItem, EdgeItem

from lab3.core.linked_queue import LinkedQueue
from lab5.core.chaining_hash_map import ChainingHashMap
from lab10.core.graph import Vertex, Graph


def breadth_first_search(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> ChainingHashMap[Vertex[VertexItem], tuple[int, Optional[Vertex[VertexItem]]]]:
    bfs_map = ChainingHashMap.build(iter([(source, (0, None))]))
    queue = LinkedQueue.build(iter([(source, 0)]))
    while not queue.is_empty():
        vertex, distance = queue.dequeue()
        distance += 1
        for neighbour in graph.neighbours(vertex):
            if not bfs_map.contains(neighbour):
                bfs_map.insert(neighbour, (distance, vertex))
                queue.enqueue((neighbour, distance))
    return bfs_map


