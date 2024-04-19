from lib.array import Array
from lib.iterator import iterator
from lib.random import shuffle
from lib.test import Test

from lab4.core.merge_sort import merge, merge_sort
from lab5.core.chaining_hash_map import ChainingHashMap
from lab10.core.graph.exercise import Vertex, Edge, Graph


@Test
def vertices_on_directed_example():
    a = Vertex(1)
    b = Vertex(2)
    c = Vertex(3)
    d = Vertex(4)
    e = Vertex(5)
    f = Vertex(6)
    g = Vertex(7)
    vertices = Array.build(iterator(a, b, c, d, e, f, g))
    edges = Array.build(
        iterator(
            Edge(a, b, None),
            Edge(b, d, None),
            Edge(b, e, None),
            Edge(d, a, None),
            Edge(d, e, None),
            Edge(e, d, None),
            Edge(f, c, None),
        )
    )
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
    )
    graph_vertices = Array.build(graph.vertices())
    merge_sort(vertices)
    merge_sort(graph_vertices)
    yield vertices
    yield graph_vertices


@Test
def vertices_on_undirected_example():
    a = Vertex(0)
    b = Vertex(1)
    c = Vertex(2)
    d = Vertex(3)
    e = Vertex(4)
    f = Vertex(5)
    vertices = Array.build(iterator(a, b, c, d, e, f))
    edges = Array.build(
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
        )
    )
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
        False,
    )
    graph_vertices = Array.build(graph.vertices())
    merge_sort(vertices)
    merge_sort(graph_vertices)
    yield vertices
    yield graph_vertices


@Test
def edges_on_directed_example():
    a = Vertex(1)
    b = Vertex(2)
    c = Vertex(3)
    d = Vertex(4)
    e = Vertex(5)
    f = Vertex(6)
    g = Vertex(7)
    vertices = Array.build(iterator(a, b, c, d, e, f, g))
    edges = Array.build(
        iterator(
            Edge(a, b, None),
            Edge(b, d, None),
            Edge(b, e, None),
            Edge(d, a, None),
            Edge(d, e, None),
            Edge(e, d, None),
            Edge(f, c, None),
        )
    )
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
    )
    graph_edges = Array.build(graph.edges())
    merge_sort(edges)
    merge_sort(graph_edges)
    yield edges
    yield graph_edges


@Test
def edges_on_undirected_example():
    a = Vertex(0)
    b = Vertex(1)
    c = Vertex(2)
    d = Vertex(3)
    e = Vertex(4)
    f = Vertex(5)
    vertices = Array.build(iterator(a, b, c, d, e, f))
    edges = Array.build(
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
        )
    )
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
        False,
    )
    graph_edges = Array.build(graph.edges())
    converse_edges = Array(edges.get_length())
    for index in range(edges.get_length()):
        edge = edges.get_at(index)
        converse_edge = Edge(edge.get_target(), edge.get_source(), edge.get_item())
        converse_edges.set_at(index, converse_edge)
    edges = merge(edges, converse_edges)
    merge_sort(edges)
    merge_sort(graph_edges)
    yield edges
    yield graph_edges


@Test
def get_edge_on_directed_example():
    a = Vertex(1)
    b = Vertex(2)
    c = Vertex(3)
    d = Vertex(4)
    e = Vertex(5)
    f = Vertex(6)
    g = Vertex(7)
    vertices = Array.build(iterator(a, b, c, d, e, f, g))
    a_b = Edge(a, b, None)
    b_d = Edge(b, d, None)
    b_e = Edge(b, e, None)
    d_a = Edge(d, a, None)
    d_e = Edge(d, e, None)
    e_d = Edge(e, d, None)
    f_c = Edge(f, c, None)
    edges = Array.build(iterator(a_b, b_d, b_e, d_a, d_e, e_d, f_c))
    edge_map = ChainingHashMap.build(
        iterator(
            ((a, b), a_b),
            ((b, d), b_d),
            ((b, e), b_e),
            ((d, a), d_a),
            ((d, e), d_e),
            ((e, d), e_d),
            ((f, c), f_c),
        ),
    )
    for vertex_a in vertices.iterator():
        for vertex_b in vertices.iterator():
            if vertex_a is vertex_b:
                continue
            vertex_pair = vertex_a, vertex_b
            if edge_map.contains(vertex_pair):
                continue
            edge_map.insert(vertex_pair, None)
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
    )
    incorrect = None
    for (vertex_a, vertex_b), correct_edge in edge_map.iterator():
        edge = graph.get_edge(vertex_a, vertex_b)
        if edge != correct_edge:
            incorrect = vertex_a, vertex_b, correct_edge, edge
            break
    yield None
    yield incorrect


@Test
def get_edge_on_undirected_example():
    a = Vertex(0)
    b = Vertex(1)
    c = Vertex(2)
    d = Vertex(3)
    e = Vertex(4)
    f = Vertex(5)
    vertices = Array.build(iterator(a, b, c, d, e, f))
    a_b = Edge(a, b, None)
    a_f = Edge(a, f, None)
    b_c = Edge(b, c, None)
    b_d = Edge(b, d, None)
    b_f = Edge(b, f, None)
    c_d = Edge(c, d, None)
    d_e = Edge(d, e, None)
    d_f = Edge(d, f, None)
    e_f = Edge(e, f, None)
    edges = Array.build(iterator(a_b, a_f, b_c, b_d, b_f, c_d, d_e, d_f, e_f))
    edge_map = ChainingHashMap.build(
        iterator(
            ((a, b), a_b),
            ((a, f), a_f),
            ((b, c), b_c),
            ((b, d), b_d),
            ((b, f), b_f),
            ((c, d), c_d),
            ((d, e), d_e),
            ((d, f), d_f),
            ((e, f), e_f),
            ((b, a), Edge(b, a, None)),
            ((f, a), Edge(f, a, None)),
            ((c, b), Edge(c, b, None)),
            ((d, b), Edge(d, b, None)),
            ((f, b), Edge(f, b, None)),
            ((d, c), Edge(d, c, None)),
            ((e, d), Edge(e, d, None)),
            ((f, d), Edge(f, d, None)),
            ((f, e), Edge(f, e, None)),
        ),
    )
    for vertex_a in vertices.iterator():
        for vertex_b in vertices.iterator():
            if vertex_a is vertex_b:
                continue
            vertex_pair = vertex_a, vertex_b
            if edge_map.contains(vertex_pair):
                continue
            edge_map.insert(vertex_pair, None)
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
        False,
    )
    incorrect = None
    for (vertex_a, vertex_b), correct_edge in edge_map.iterator():
        edge = graph.get_edge(vertex_a, vertex_b)
        if edge != correct_edge:
            incorrect = vertex_a, vertex_b, correct_edge, edge
            break
    yield None
    yield incorrect


@Test
def degree_on_directed_example():
    a = Vertex(1)
    b = Vertex(2)
    c = Vertex(3)
    d = Vertex(4)
    e = Vertex(5)
    f = Vertex(6)
    g = Vertex(7)
    vertices = Array.build(iterator(a, b, c, d, e, f, g))
    a_b = Edge(a, b, None)
    b_d = Edge(b, d, None)
    b_e = Edge(b, e, None)
    d_a = Edge(d, a, None)
    d_e = Edge(d, e, None)
    e_d = Edge(e, d, None)
    f_c = Edge(f, c, None)
    edges = Array.build(iterator(a_b, b_d, b_e, d_a, d_e, e_d, f_c))
    degree_map = ChainingHashMap.build(
        iterator(
            (a, 1),
            (b, 2),
            (c, 0),
            (d, 2),
            (e, 1),
            (f, 1),
            (g, 0),
        ),
    )
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
    )
    incorrect = None
    for vertex, correct_degree in degree_map.iterator():
        degree = graph.degree(vertex)
        if degree != correct_degree:
            incorrect = vertex, correct_degree, degree
            break
    yield None
    yield incorrect


@Test
def degree_on_undirected_example():
    a = Vertex(0)
    b = Vertex(1)
    c = Vertex(2)
    d = Vertex(3)
    e = Vertex(4)
    f = Vertex(5)
    vertices = Array.build(iterator(a, b, c, d, e, f))
    a_b = Edge(a, b, None)
    a_f = Edge(a, f, None)
    b_c = Edge(b, c, None)
    b_d = Edge(b, d, None)
    b_f = Edge(b, f, None)
    c_d = Edge(c, d, None)
    d_e = Edge(d, e, None)
    d_f = Edge(d, f, None)
    e_f = Edge(e, f, None)
    edges = Array.build(iterator(a_b, a_f, b_c, b_d, b_f, c_d, d_e, d_f, e_f))
    degree_map = ChainingHashMap.build(
        iterator(
            (a, 2),
            (b, 4),
            (c, 2),
            (d, 4),
            (e, 2),
            (f, 4),
        ),
    )
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
        False,
    )
    incorrect = None
    for vertex, correct_degree in degree_map.iterator():
        degree = graph.degree(vertex)
        if degree != correct_degree:
            incorrect = vertex, correct_degree, degree
            break
    yield None
    yield incorrect


@Test
def neighbours_on_directed_example():
    a = Vertex(1)
    b = Vertex(2)
    c = Vertex(3)
    d = Vertex(4)
    e = Vertex(5)
    f = Vertex(6)
    g = Vertex(7)
    vertices = Array.build(iterator(a, b, c, d, e, f, g))
    a_b = Edge(a, b, None)
    b_d = Edge(b, d, None)
    b_e = Edge(b, e, None)
    d_a = Edge(d, a, None)
    d_e = Edge(d, e, None)
    e_d = Edge(e, d, None)
    f_c = Edge(f, c, None)
    edges = Array.build(iterator(a_b, b_d, b_e, d_a, d_e, e_d, f_c))
    neighbours_map = ChainingHashMap.build(
        iterator(
            (a, Array.build(iterator(b))),
            (b, Array.build(iterator(d, e))),
            (c, Array.build(iterator())),
            (d, Array.build(iterator(a, e))),
            (e, Array.build(iterator(d))),
            (f, Array.build(iterator(c))),
            (g, Array.build(iterator())),
        ),
    )
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
    )
    incorrect = None
    for vertex, correct_neighbours in neighbours_map.iterator():
        neighbours = Array.build(graph.neighbours(vertex))
        merge_sort(neighbours)
        merge_sort(correct_neighbours)
        if neighbours != correct_neighbours:
            incorrect = vertex, correct_neighbours, neighbours
            break
    yield None
    yield incorrect


@Test
def neighbours_on_undirected_example():
    a = Vertex(0)
    b = Vertex(1)
    c = Vertex(2)
    d = Vertex(3)
    e = Vertex(4)
    f = Vertex(5)
    vertices = Array.build(iterator(a, b, c, d, e, f))
    a_b = Edge(a, b, None)
    a_f = Edge(a, f, None)
    b_c = Edge(b, c, None)
    b_d = Edge(b, d, None)
    b_f = Edge(b, f, None)
    c_d = Edge(c, d, None)
    d_e = Edge(d, e, None)
    d_f = Edge(d, f, None)
    e_f = Edge(e, f, None)
    edges = Array.build(iterator(a_b, a_f, b_c, b_d, b_f, c_d, d_e, d_f, e_f))
    neighbours_map = ChainingHashMap.build(
        iterator(
            (a, Array.build(iterator(b, f))),
            (b, Array.build(iterator(a, c, d, f))),
            (c, Array.build(iterator(b, d))),
            (d, Array.build(iterator(b, c, e, f))),
            (e, Array.build(iterator(d, f))),
            (f, Array.build(iterator(a, b, d, e))),
        ),
    )
    shuffle(vertices)
    shuffle(edges)
    graph = Graph(
        vertices.iterator(),
        edges.iterator(),
        False,
    )
    incorrect = None
    for vertex, correct_neighbours in neighbours_map.iterator():
        neighbours = Array.build(graph.neighbours(vertex))
        merge_sort(neighbours)
        merge_sort(correct_neighbours)
        if neighbours != correct_neighbours:
            incorrect = vertex, correct_neighbours, neighbours
            break
    yield None
    yield incorrect
