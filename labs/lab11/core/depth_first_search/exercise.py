"""
Data Structures & Algorithms

Lab 11: More Graph Algorithms

Depth-first Search Exercise
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
    raise NotImplementedError


def depth_first_search(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> tuple[ChainingHashMap[Vertex[VertexItem], Optional[Vertex[VertexItem]]], DynamicArrayList[Vertex[VertexItem]]]:
    raise NotImplementedError


def full_depth_first_search(
    graph: Graph[VertexItem, EdgeItem],
) -> tuple[ChainingHashMap[Vertex[VertexItem], Optional[Vertex[VertexItem]]], DynamicArrayList[Vertex[VertexItem]]]:
    raise NotImplementedError
