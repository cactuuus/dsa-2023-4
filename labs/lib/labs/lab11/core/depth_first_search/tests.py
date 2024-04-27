from collections.abc import Iterator

from lib.array import Array
from lib.iterator import iterator
from lib.test import Test
from lib.type_vars import VertexItem, EdgeItem

from lab3.core.dynamic_array_list import DynamicArrayList
from lab4.core.merge_sort import merge_sort
from lab4.core.sorted_array_map import SortedArrayMap
from lab10.core.graph import Vertex, Edge, Graph
from lab11.core.depth_first_search.exercise import depth_first_search, full_depth_first_search


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
def paths_of_depth_first_search_from_3_on_directed_example():
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
            (c, None),
        )
    )
    paths, visited = depth_first_search(graph, c)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def visited_of_depth_first_search_from_3_on_directed_example():
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
    correct_visited = Array.build(iterator(c))
    paths, visited = depth_first_search(graph, c)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_depth_first_search_from_4_on_directed_example():
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
            (a, d),
            (b, a),
            (d, None),
            (e, b),
        )
    )
    paths, visited = depth_first_search(graph, d)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def visited_of_depth_first_search_from_4_on_directed_example():
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
    correct_visited = Array.build(iterator(e, b, a, d))
    paths, visited = depth_first_search(graph, d)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_depth_first_search_from_6_on_directed_example():
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
            (f, None),
            (c, f),
        )
    )
    paths, visited = depth_first_search(graph, f)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def visited_of_depth_first_search_from_6_on_directed_example():
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
    correct_visited = Array.build(iterator(c, f))
    paths, visited = depth_first_search(graph, f)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_depth_first_search_from_7_on_directed_example():
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
            (g, None),
        )
    )
    paths, visited = depth_first_search(graph, g)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def visited_of_depth_first_search_from_7_on_directed_example():
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
    correct_visited = Array.build(iterator(g))
    paths, visited = depth_first_search(graph, g)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_depth_first_search_from_0_on_undirected_example():
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
            (a, None),
            (b, a),
            (c, b),
            (d, c),
            (e, d),
            (f, e),
        )
    )
    paths, visited = depth_first_search(graph, a)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def vertices_of_depth_first_search_from_0_on_undirected_example():
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
    correct_visited = Array.build(iterator(f, e, d, c, b, a))
    paths, visited = depth_first_search(graph, a)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_depth_first_search_from_1_on_undirected_example():
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
            (a, b),
            (b, None),
            (c, d),
            (d, f),
            (e, d),
            (f, a),
        )
    )
    paths, visited = depth_first_search(graph, b)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def vertices_of_depth_first_search_from_1_on_undirected_example():
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
    correct_visited = Array.build(iterator(c, e, d, f, a, b))
    paths, visited = depth_first_search(graph, b)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_depth_first_search_from_2_on_undirected_example():
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
            (a, b),
            (b, c),
            (c, None),
            (d, f),
            (e, d),
            (f, a),
        )
    )
    paths, visited = depth_first_search(graph, c)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def vertices_of_depth_first_search_from_2_on_undirected_example():
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
    correct_visited = Array.build(iterator(e, d, f, a, b, c))
    paths, visited = depth_first_search(graph, c)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_depth_first_search_from_3_on_undirected_example():
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
            (a, b),
            (b, d),
            (c, b),
            (d, None),
            (e, f),
            (f, a),
        )
    )
    paths, visited = depth_first_search(graph, d)
    paths = Array.build(paths.iterator())
    merge_sort(correct_paths)
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def vertices_of_depth_first_search_from_3_on_undirected_example():
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
    correct_visited = Array.build(iterator(e, f, a, c, b, d))
    paths, visited = depth_first_search(graph, d)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_full_depth_first_search_on_directed_example():
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
            (a, None),
            (b, a),
            (c, None),
            (d, b),
            (e, d),
            (f, None),
            (g, None),
        )
    )
    merge_sort(correct_paths)
    paths, visited = full_depth_first_search(graph)
    paths = Array.build(paths.iterator())
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def visited_of_full_depth_first_search_on_directed_example():
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
    correct_visited = Array.build(iterator(e, d, b, a, c, f, g))
    paths, visited = full_depth_first_search(graph)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited


@Test
def paths_of_full_depth_first_search_on_undirected_example():
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
            (a, None),
            (b, a),
            (c, b),
            (d, c),
            (e, d),
            (f, e),
        )
    )
    merge_sort(correct_paths)
    paths, visited = full_depth_first_search(graph)
    paths = Array.build(paths.iterator())
    merge_sort(paths)
    yield correct_paths
    yield paths


@Test
def visited_of_full_depth_first_search_on_undirected_example():
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
    correct_visited = Array.build(iterator(f, e, d, c, b, a))
    paths, visited = full_depth_first_search(graph)
    visited = Array.build(visited.iterator())
    yield correct_visited
    yield visited
