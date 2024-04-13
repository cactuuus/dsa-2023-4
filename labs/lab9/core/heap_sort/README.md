# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 9: Binary Heaps & Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/README.md))

### [Heap Sort](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/heap_sort/README.md)
```shell
python labs heap_sort
```

We start with heap sort. Though, what you're actually asked to implement isn't heap sort itself, but the max-heapify-up
and max-heapify-down operations it uses. This is mainly to get you warmed up - and your brain thinking about heaps -
ahead of the next exercise, which is to implement a more general binary heap.

In this exercise, we want the array's items to be sorted into ascending order, so - as explained in the lectures - we
use a max-heap. (In the next exercise, we'll have our heap be configurable via a parameter to be either max or min.)

As a reminder: Because binary heaps are complete binary trees* (and, more generally, heaps are complete trees), we can
efficiently represent them using a flat list, with the hierarchical tree structure implicit.

\* Every binary heap is a complete binary tree, but not every complete binary tree is a binary heap.

For example,

![(((7) 15 (10)) 90 ((60) 75 (50))) 100 (((10) 30 ()) 46 (25))](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lib/resources/binary_heap/heap.png)

can be represented as
```python
[100, 90, 46, 15, 75, 30, 25, 7, 10, 60, 50, 10]
```

The list contains the first level, then the second level, then the third, then the fourth.
```
           .------>------.
       .---+->---.       |
       |   |   .-'-.   .-'-.
[100, 90, 46, 15, 75, 30, 25,  7, 10, 60, 50, 10]
 |     '-.-'   |   |   |       '-.-'   '-.-'   '-.
 '--->---'     '---+---+->-------'       |       |
                   '---+------>----------'       |
                       '------------>------------'
```

Further, in this exercise, we're representing the heap as a prefix of the given array. The array's length never changes
(we're only sorting it, not inserting/removing), but we build up a heap within it from the left, and _its_ length grows
from 0 to the whole array, before we break it back down again, leaving the array's items sorted. For a better reminder
of how this all works, see the lecture slides.

When implementing `_max_heapify_up` and `_max_heapify_down`, you'll likely want to consult the slides' pseudocode. (If
you'd like, feel free to figure out how to implement them iteratively rather than recursively. Either way, good luck!)

---

Next:
- [Binary Heaps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/binary_heap/README.md)
