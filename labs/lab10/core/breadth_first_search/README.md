# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 10: Graphs & Breadth-first Search](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab10/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab10/core/README.md))

### [Breadth-first Search](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab10/core/breadth_first_search/README.md)
```shell
python labs breadth_first_search
```

Now we're going to implement breadth-first search, though slightly differently to the pseudocode of the lectures.

The difference is that, rather than storing data on the vertices, we're going to make a map that will contain it.

Your implementation shouldn't modify the graph that it's given. It should instead create a map from the reachable
vertices to their shortest path information, in the form of the distance and the predecessor. (Vertices that aren't
reachable from the given source vertex, which are those that in the lectures would have a distance of infinity,
shouldn't have an entry in the map.) You should create this map at the start of the function, build it up as you go,
and then return it as the output of the function. (You will hopefully see that you can substitute the check for whether
a vertex is white with one for whether it has an entry in the map.)

Despite this difference, your implementation will likely still look very similar to the pseudocode presented in the
lectures. Good luck figuring it out - once you have, you'll have just one more lab to go!
