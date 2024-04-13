# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 9: Binary Heaps & Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/README.md))

### [Binary Heaps](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/binary_heap/README.md)
```shell
python labs binary_heap
```

In this exercise we're implementing a more general binary heap. Many of its operations will be similar to our map
types', but here what we'll really be implementing is a "multi-map" - i.e. one that can have multiple values
associated with the same key.

The heap we're implementing will take, as an optional initialization parameter, a boolean indicating whether it should
be a max-heap or a min-heap (with max being the default). Because of this, we'll talk about e.g. `remove_root` rather
than `remove_max`, to be agnostic about whether the root is the maximum or the minimum. Speaking of the operations,
you're asked to implement the three main ones, namely

1. `insert`
2. `get_root`
3. `remove_root`

as well as the two auxiliary operations (which you should use in your implementations of the ones above)

1. `_heapify_up`
2. `_heapify_down`

Assuming you completed the previous exercise, you should be able to adapt your implementations of `_max_heapify_up` and
`_max_heapify_down` reasonably straightforwardly - the main thing to change is to generalise the comparisons, so that
they work correctly regardless of whether it's a max-heap or min-heap. (You will likely find the `_has_greater_key`
method useful for this.)

Again: Have the lecture slides in hand, and you should hopefully be able to figure it out.

(If you look at `build`, you'll see that it uses `_heapify_down`, so therefore various tests that might not otherwise
require `_heapify_down` will fail if it's not implemented, so that's probably a good place to start!)

---

Next:
- [Unsorted List Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/unsorted_list_priority_queue/README.md)
