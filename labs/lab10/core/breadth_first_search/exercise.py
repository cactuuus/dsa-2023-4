from typing import Optional
from lib.type_vars import VertexItem, EdgeItem

from lab3.core.linked_queue import LinkedQueue
from lab5.core.chaining_hash_map import ChainingHashMap
from lab10.core.graph import Vertex, Graph


def breadth_first_search(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> ChainingHashMap[Vertex[VertexItem], tuple[int, Optional[Vertex[VertexItem]]]]:
    raise NotImplementedError
