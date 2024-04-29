# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 11: More Graph Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab11/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab11/core/README.md))

### [Depth-first Search](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab11/core/depth_first_search/README.md)
```shell
python labs depth_first_search
```

First, we're going to implement depth-first search, as well as full depth-first search, both in terms of `_dfs_visit`.

(You could alternatively implement full depth-first search instead of depth-first search, but we're not going to do that here.)

Similarly to the breadth-first search exercise last lab, the functions we're implementing have slightly different type
signatures to the operations described in the lectures.

You'll notice that our `depth_first_search` has a very similar signature to `breadth_first_search`:
```python
def breadth_first_search(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> ChainingHashMap[Vertex[VertexItem], tuple[int, Optional[Vertex[VertexItem]]]]:
```
```python
def depth_first_search(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> tuple[ChainingHashMap[Vertex[VertexItem], Optional[Vertex[VertexItem]]], DynamicArrayList[Vertex[VertexItem]]]:
```

The difference is, of course, in their return types. Simplified, they are:
```python
bfs -> Map[Vertex, tuple[int, Optional[Vertex]]]
dfs -> tuple[Map[Vertex, Optional[Vertex]], List[Vertex]]
```

Both BFS and DFS return a map from reachable vertices to information about the paths they found to those vertices.

With BFS, that information was the number of steps to that vertex (from the given source / starting vertex), as well as
the predecessor / previous vertex on the path from the source to that vertex.

We were particularly including the length of the path as the path found by BFS is (assuming the given graph isn't
weighted) the shortest path.

With DFS, however, we're not looking for (nor would we likely get) the shortest path, and instead are mainly just
interested in whether the vertex is reachable at all. We get this from the keys of the map (as we're only going to
include entries for reachable vertices), but as well as providing the set of vertices reachable from the given source,
we provide an actual path (in the same way, i.e. by giving predecessors) for each of those vertices. This is both as a
sort of existence proof for their reachability, and also because - depending on the application - we may well be
interested in finding actual paths, not just determining whether there are any.

The other difference with DFS, apart from not worrying about returning the paths' distances, is that we additionally
return the vertices we visited (which are the reachable vertices) as a list in the order that we finished visited them.
(This is the same as in the lectures.)

Full DFS is much the same, but - as in the lectures - it doesn't take a starting vertex, and instead essentially tries
starting from every vertex, and thus all of the graph's vertices will be in the returned list and will be keys in the
returned map.

`_dfs_visit`, the function that they're both to be implemented in terms of, is essentially the same as the slides'
DFS-Visit procedure, with the differences being the same differences as those already explained (to do with returning a
map rather than modifying the graph's vertices).

If you managed last week's BFS exercise, you should hopefully be able to figure it out. Otherwise, it may be worth
looking at its solution first. Either way, good luck!

---

Next:
- [Topological Sort](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab11/core/topological_sort/README.md)
