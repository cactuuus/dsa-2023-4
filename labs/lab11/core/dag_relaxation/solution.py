"""
Data Structures & Algorithms

Lab 11: More Graph Algorithms

DAG Relaxation Solution
"""

from typing import Optional

from lib.type_vars import VertexItem, EdgeItem

from lab5.core.chaining_hash_map import ChainingHashMap
from lab10.core.graph import Vertex, Graph
from lab11.core.topological_sort import topologically_sorted_vertices


def dag_relaxation(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> ChainingHashMap[Vertex[VertexItem], tuple[int, Optional[Vertex[VertexItem]]]]:
    paths = ChainingHashMap()
    paths.insert(source, (0, None))
    for vertex in topologically_sorted_vertices(graph):
        if not paths.contains(vertex):
            continue
        distance, _ = paths.get(vertex)
        for neighbour in graph.neighbours(vertex):
            edge = graph.get_edge(vertex, neighbour)
            weight = edge.get_item()
            neighbour_distance = distance + weight
            if paths.contains(neighbour):
                old_neighbour_distance, _ = paths.get(neighbour)
                if old_neighbour_distance <= neighbour_distance:
                    continue
            paths.insert(neighbour, (neighbour_distance, vertex))
    return paths
