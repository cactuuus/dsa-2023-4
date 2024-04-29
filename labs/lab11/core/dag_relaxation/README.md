# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 11: More Graph Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab11/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab11/core/README.md))

### [DAG Relaxation](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab11/core/dag_relaxation/README.md)
```shell
python labs dag_relaxation
```

And now we come to the last exercise - not just of the lab, but of the labs!

If you're looking for more fun(!), you may enjoy reimplementing some of these data structures and algorithms in other
languages. If you've been disappointed that the last few labs haven't had any plus content, then you may be pleased to
hear that some will be added soon. You may, of course, be needing/wanting to really focus on revision as the end-of-year
exams approach, but once those are done, and you've had your fill of summer, you might check back here, have another
look at the exercises, catch up with the "plus' content, and have a go at alternative ways to implement these things. Or
you might not. Either way, hopefully you've enjoyed and learnt from all this. Almost all that remains to be said is good
luck with the exam(s)!

_Almost_ all, that is. There is one more exercise, after all.

That exercise - this exercise - is implementing the DAG relaxation algorithm.

Our implementation will again be slightly different to the slides' pseudocode. Similarly to the BFS and DFS exercises,
we're not going to modify the given graph, but instead return a map from reachable vertices to their path information.
In fact, what we're going to do is almost exactly the same as for BFS, in that the information we're going to return for
each reachable vertex is the length of the shortest path from the given source to that vertex, as well as the
penultimate vertex on such a path:
```python
def breadth_first_search(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> ChainingHashMap[Vertex[VertexItem], tuple[int, Optional[Vertex[VertexItem]]]]:
```
```python
def dag_relaxation(
    graph: Graph[VertexItem, EdgeItem],
    source: Vertex[VertexItem],
) -> ChainingHashMap[Vertex[VertexItem], tuple[int, Optional[Vertex[VertexItem]]]]:
```

The difference is that we're going to treat the graph we're given as a weighted DAG.

The particular point is that we're going to assume `EdgeItem` is some type that represents the weight/cost/distance
between two vertices, and then say that the length of a path, rather than being the number of edges as in BFS, is the
sum of the edges' weights.

As for the implementation, the slides give the idea, and though our Python will differ from the pseudocode, given that
it's the same difference as in the BFS and DFS exercises, you should hopefuly be able to convert from one to the other.

We haven't included stubs for `_initialise_single_source`/`_relax` functions, as you may prefer to implement them (or
their equivalents) directly in `dag_relaxation`, but if you'd prefer, you are of course free to define them as helpers.

Right, that's enough lab notes for one term! Good luck with the exercise, the exam(s), and enjoy some well-earned relaxation!
