from collections.abc import Iterator

from lib.array import Array
from lib.iterator import iterator
from lib.test import Test
from lib.type_vars import VertexItem, EdgeItem

from lab3.core.dynamic_array_list import DynamicArrayList
from lab4.core.sorted_array_map import SortedArrayMap
from lab10.core.graph import Vertex, Edge, Graph
from lab11.core.topological_sort.exercise import topologically_sorted_vertices


Graph_ = Graph


def Graph(
    vertices: Iterator[Vertex[VertexItem]],
    edges: Iterator[Edge[VertexItem, EdgeItem]],
    is_directed: bool = True,
) -> Graph_:
    graph = Graph_(iterator(), iterator(), is_directed)
    graph._map = SortedArrayMap()
    for vertex in vertices:
        graph._map.insert(vertex, DynamicArrayList())
    for edge in edges:
        source = edge.get_source()
        target = edge.get_target()
        edges_from_source = graph._map.get(source)
        edges_from_target = graph._map.get(target)
        edges_from_source.insert_last(edge)
        if not is_directed:
            converse = Edge(target, source, edge.get_item())
            edges_from_target.insert_last(converse)
    return graph


@Test
def visited_of_topologically_sorted_vertices_on_directed_example():
    a = Vertex(1)
    b = Vertex(2)
    c = Vertex(3)
    d = Vertex(4)
    e = Vertex(5)
    f = Vertex(6)
    g = Vertex(7)
    graph = Graph(
        iterator(a, b, c, d, e, f, g),
        iterator(
            Edge(a, b, None),
            Edge(b, d, None),
            Edge(b, e, None),
            Edge(d, a, None),
            Edge(d, e, None),
            Edge(e, d, None),
            Edge(f, c, None),
        ),
    )
    correct_vertices = Array.build(iterator(g, f, c, a, b, d, e))
    vertices = Array.build(topologically_sorted_vertices(graph))
    yield correct_vertices
    yield vertices


@Test
def visited_of_topologically_sorted_vertices_on_undirected_example():
    a = Vertex(0)
    b = Vertex(1)
    c = Vertex(2)
    d = Vertex(3)
    e = Vertex(4)
    f = Vertex(5)
    graph = Graph(
        iterator(a, b, c, d, e, f),
        iterator(
            Edge(a, b, None),
            Edge(a, f, None),
            Edge(b, c, None),
            Edge(b, d, None),
            Edge(b, f, None),
            Edge(c, d, None),
            Edge(d, e, None),
            Edge(d, f, None),
            Edge(e, f, None),
        ),
        False,
    )
    correct_vertices = Array.build(iterator(a, b, c, d, e, f))
    vertices = Array.build(topologically_sorted_vertices(graph))
    yield correct_vertices
    yield vertices
