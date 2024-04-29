"""
Data Structures & Algorithms

Lab 11: More Graph Algorithms

DAG Relaxation Exercise
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
    raise NotImplementedError
