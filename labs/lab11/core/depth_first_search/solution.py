"""
Data Structures & Algorithms

Lab 11: More Graph Algorithms

Depth-first Search Solution
"""

from typing import Optional

from lib.type_vars import VertexItem, EdgeItem

from lab3.core.dynamic_array_list import DynamicArrayList
from lab5.core.chaining_hash_map import ChainingHashMap
from lab10.core.graph import Vertex, Graph


def _dfs_visit(
    graph: Graph[VertexItem, EdgeItem],
    vertex: Vertex[VertexItem],
    paths: ChainingHashMap[Vertex[VertexItem], Optional[Vertex[VertexItem]]],
    visited: DynamicArrayList[Vertex[VertexItem]],
) -> None:
    for neighbour in graph.neighbours(vertex):
        if not paths.contains(neighbour):
            paths.insert(neighbour, vertex)
            _dfs_visit(graph, neighbour, paths, visited)
    visited.insert_last(vertex)


def depth_first_search(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> tuple[ChainingHashMap[Vertex[VertexItem], Optional[Vertex[VertexItem]]], DynamicArrayList[Vertex[VertexItem]]]:
    paths = ChainingHashMap()
    paths.insert(source, None)
    visited = DynamicArrayList()
    _dfs_visit(graph, source, paths, visited)
    return paths, visited


def full_depth_first_search(
    graph: Graph[VertexItem, EdgeItem],
) -> tuple[ChainingHashMap[Vertex[VertexItem], Optional[Vertex[VertexItem]]], DynamicArrayList[Vertex[VertexItem]]]:
    paths = ChainingHashMap()
    visited = DynamicArrayList()
    for vertex in graph.vertices():
        if not paths.contains(vertex):
            paths.insert(vertex, None)
            _dfs_visit(graph, vertex, paths, visited)
    return paths, visited
