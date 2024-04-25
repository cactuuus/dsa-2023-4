from lib.array import Array
from lib.iterator import iterator
from lib.test import Test

from lab4.core.merge_sort import merge_sort
from lab10.core.graph import Vertex, Edge, Graph
from lab10.core.breadth_first_search.exercise import breadth_first_search


@Test
def breadth_first_search_from_4_on_directed_example():
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
    correct_paths = Array.build(
        iterator(
            (a, (1, d)),
            (b, (2, a)),
            (d, (0, None)),
            (e, (1, d)),
        )
    )
    paths = Array.build(breadth_first_search(graph, d).iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def breadth_first_search_from_0_on_undirected_example():
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
    correct_paths = Array.build(
        iterator(
            (a, (0, None)),
            (b, (1, a)),
            (c, (2, b)),
            (d, (2, b)),
            (e, (2, f)),
            (f, (1, a)),
        )
    )
    paths = Array.build(breadth_first_search(graph, a).iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths
