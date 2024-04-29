"""
Data Structures & Algorithms

Lab 10: Graphs & Breadth-first Search

Breadth-first Search Solution
"""

from typing import Optional
from lib.type_vars import VertexItem, EdgeItem

from lab3.core.linked_queue import LinkedQueue
from lab5.core.chaining_hash_map import ChainingHashMap
from lab10.core.graph import Vertex, Graph


def breadth_first_search(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> ChainingHashMap[Vertex[VertexItem], tuple[int, Optional[Vertex[VertexItem]]]]:
    frontier = LinkedQueue()
    frontier.enqueue(source)
    paths = ChainingHashMap()
    paths.insert(source, (0, None))
    while not frontier.is_empty():
        vertex = frontier.dequeue()
        distance, _ = paths.get(vertex)
        new_path = distance + 1, vertex
        for neighbour in graph.neighbours(vertex):
            if not paths.contains(neighbour):
                frontier.enqueue(neighbour)
                paths.insert(neighbour, new_path)
    return paths
