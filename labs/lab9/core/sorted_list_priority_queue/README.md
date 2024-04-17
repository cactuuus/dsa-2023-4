# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 9: Binary Heaps & Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/README.md))

### [Sorted List Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/sorted_list_priority_queue/README.md)
```shell
python labs sorted_list_priority_queue
```

This type of priority queue is like the previous, in that it stores its items in a list, but it does so differently.

What it does differently is that it stores them in order (of priority). When enqueueing, it finds the place in the list
where the item should go, and inserts it there, maintaining the sortedness of the list. For example, if the list
contains items with priorities `[2, 4, 7, 8]`, and the item to enqueue has priority `3`, it will be inserted at index
`1`, resulting in `[2, 3, 4, 7, 8]`.

Although this makes for a less efficient enqueue operation, the advantage is that dequeueing can be done in (amortized)
constant time, as the next item to be dequeued is always the last in the list.

(Note: If you'd like to improve the efficiency of `enqueue`, you could use binary search. However, unless you have
unique priorities, or don't care about the stability of the corresponding PQ sort / FIFO behaviour for equal priorities,
you won't improve the worst case time complexity from linear to logarithmic. This is because, having performed binary
search, if you find there is already an item with the same priority as the one you're inserting, you would then need to
linearly scan left until you find the leftmost item with that same priority, so that you can insert the new one left of
that. Most or all of the items might have the same priority, in which case it would be no improvement. That said, for
most cases, first performing binary search would improve performance, though we're not expecting you to do that here.
Incidentally, sorted list priority queues only correspond to insertion sort if linear search is used in `enqueue`. If
binary search is used, then it instead correlates to binary insertion sort.)

---

Next:
- [AVL Tree Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/avl_tree_priority_queue/README.md)
