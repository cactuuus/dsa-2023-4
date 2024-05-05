"""
Data Structures & Algorithms

Lab 11: More Graph Algorithms

Topological Sort Solution
"""

from collections.abc import Iterator

from lib.type_vars import VertexItem, EdgeItem

from lab10.core.graph import Vertex, Graph
from lab11.core.depth_first_search import full_depth_first_search


def topologically_sorted_vertices(graph: Graph[VertexItem, EdgeItem]) -> Iterator[Vertex[VertexItem]]:
    _, visited = full_depth_first_search(graph)
    return visited.reverse_iterator()
