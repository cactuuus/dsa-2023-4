from collections.abc import Iterator

from lib.array import Array
from lib.iterator import iterator
from lib.test import Test
from lib.type_vars import VertexItem, EdgeItem

from lab3.core.dynamic_array_list import DynamicArrayList
from lab4.core.merge_sort import merge_sort
from lab4.core.sorted_array_map import SortedArrayMap
from lab10.core.graph import Vertex, Edge, Graph
from lab11.core.dag_relaxation.exercise import dag_relaxation


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
def dag_relaxation_from_b_on_example():
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")
    g = Vertex("g")
    h = Vertex("h")
    graph = Graph(
        iterator(a, b, c, d, e, f, g, h),
        iterator(
            Edge(a, b, -5),
            Edge(a, e, 7),
            Edge(b, c, -1),
            Edge(b, e, 6),
            Edge(b, f, -4),
            Edge(d, c, 5),
            Edge(e, f, 3),
            Edge(f, c, 8),
            Edge(f, g, 2),
            Edge(g, c, 1),
            Edge(g, h, -2),
            Edge(h, c, 9),
            Edge(h, d, 4),
        ),
    )
    correct_paths = Array.build(
        iterator(
            (b, (0, None)),
            (c, (-1, b)),
            (d, (0, h)),
            (e, (6, b)),
            (f, (-4, b)),
            (g, (-2, f)),
            (h, (-4, g)),
        )
    )
    paths = dag_relaxation(graph, b)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


# TODO
