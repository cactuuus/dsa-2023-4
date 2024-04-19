"""
Data Structures & Algorithms

Lab 10: Graphs & Breadth-first Search

Graphs Exercise
"""

from collections.abc import Iterator
from typing import Optional

from lib.base import Base
from lib.type_vars import VertexItem, EdgeItem

from lab3.core.dynamic_array_list import DynamicArrayList
from lab5.core.chaining_hash_map import ChainingHashMap


class Vertex(Base[VertexItem]):
    """
    An vertex in a graph.
    """

    _item: VertexItem

    def __init__(self, item: VertexItem) -> None:
        """
        Initialize the vertex.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter item: the vertex data
        """
        self._item = item

    def get_item(self) -> VertexItem:
        """
        Get this vertex's data.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the vertex data.
        """
        return self._item


class Edge(Base[VertexItem, EdgeItem]):
    """
    An edge in a graph.
    """

    _source: Vertex[VertexItem]
    _target: Vertex[VertexItem]
    _item: EdgeItem

    def __init__(self, source: Vertex[VertexItem], target: Vertex[VertexItem], item: EdgeItem) -> None:
        """
        Initialize the edge.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter source: the source vertex
        :parameter target: the target vertex
        :parameter item: the edge data
        :raises ValueError: if ``source`` and ``target`` are the same vertex
        """
        if source is target:
            raise ValueError
        self._source = source
        self._target = target
        self._item = item

    def get_source(self) -> Vertex[VertexItem]:
        """
        Get this edge's source vertex.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the source vertex
        """
        return self._source

    def get_target(self) -> Vertex[VertexItem]:
        """
        Get this edge's target vertex.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the target vertex
        """
        return self._target

    def get_item(self) -> EdgeItem:
        """
        Get this edge's data.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the edge data
        """
        return self._item


class Graph(Base[VertexItem, EdgeItem]):
    """
    An adjacency list graph.

    Space: O(length(vertices) + length(edges))
    """

    _is_directed: bool
    _map: ChainingHashMap[Vertex[VertexItem], DynamicArrayList[Edge[VertexItem, EdgeItem]]]

    def __init__(
        self,
        vertices: Iterator[Vertex[VertexItem]],
        edges: Iterator[Edge[VertexItem, EdgeItem]],
        is_directed: bool = True,
    ) -> None:
        """
        Initialize the graph.

        +--------+--------------------------------------------------------+
        | Time:  | O(length(vertices) + length(edges)) amortised expected |
        +--------+--------------------------------------------------------+
        | Space: | O(1)                                                   |
        +--------+--------------------------------------------------------+

        :parameter vertices: the vertices
        :parameter edges: the edges
        :parameter is_directed: whether the graph is directed (default ``True``)
        :raises KeyError: if an edge's source or target isn't among the vertices given
        :raises ValueError: if multiple edges have the same source and the same target
        """
        self._is_directed = is_directed
        self._map = ChainingHashMap()
        for vertex in vertices:
            self._map.insert(vertex, DynamicArrayList())
        for edge in edges:
            source = edge.get_source()
            target = edge.get_target()
            edges_from_source = self._map.get(source)
            edges_from_target = self._map.get(target)
            edges_from_source.insert_last(edge)
            if not is_directed:
                converse = Edge(target, source, edge.get_item())
                edges_from_target.insert_last(converse)

    def is_directed(self) -> bool:
        """
        Check if this graph is directed.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if the graph is directed, else ``False``
        """
        return self._is_directed

    def vertices(self) -> Iterator[Vertex[VertexItem]]:
        """
        Return an iterator over the vertices in this graph.
        The iteration order is unspecified.

        +--------+----------------------------+
        | Time:  | O(length(self.vertices())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: an iterator over the graph's vertices
        """
        raise NotImplementedError

    def edges(self) -> Iterator[Edge[VertexItem, EdgeItem]]:
        """
        Return an iterator over the edges in this graph.
        The iteration order is unspecified.

        +--------+-------------------------+
        | Time:  | O(length(self.edges())) |
        +--------+-------------------------+
        | Space: | O(1)                    |
        +--------+-------------------------+

        :returns: an iterator over the graph's edges
        """
        raise NotImplementedError

    def get_edge(self, source: Vertex[VertexItem], target: Vertex[VertexItem]) -> Optional[Edge[VertexItem, EdgeItem]]:
        """
        Get the edge between the given source and target if there is one, else ``None``.

        +--------+------------------------------------+
        | Time:  | O(length(self.neighbours(source))) |
        +--------+------------------------------------+
        | Space: | O(1)                               |
        +--------+------------------------------------+

        :parameter source: the source vertex
        :parameter target: the target vertex
        :returns: the edge between ``source`` and ``target`` if there is one, else ``None``
        """
        raise NotImplementedError

    def degree(self, vertex: Vertex[VertexItem]) -> int:
        """
        Get the degree of the given vertex.

        +--------+---------------+
        | Time:  | O(1) expected |
        +--------+---------------+
        | Space: | O(1)          |
        +--------+---------------+

        :parameter vertex: the vertex
        :returns: the degree of ``vertex``
        :raises KeyError: if ``vertex`` is not in the graph
        """
        raise NotImplementedError

    def neighbours(self, vertex: Vertex[VertexItem]) -> Iterator[Vertex[VertexItem]]:
        """
        Return an iterator over the neighbours of the given vertex.
        The iteration order is unspecified.

        +--------+---------------------------------------------+
        | Time:  | O(length(self.neighbours(vertex))) expected |
        +--------+---------------------------------------------+
        | Space: | O(1)                                        |
        +--------+---------------------------------------------+

        :returns: an iterator over the vertex's neighbours
        :raises KeyError: if ``vertex`` is not in the graph
        """
        raise NotImplementedError
