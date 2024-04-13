# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 9: Binary Heaps & Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/README.md))

### [Binary Heap Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/binary_heap_priority_queue/README.md)
```shell
python labs binary_heap_priority_queue
```

Now, for the most important exercise of the lab. This is somewhat backwards, because you will hopefully find it the
easiest to implement, but it is the style of priority queue most often used.*

\* (Or rather, heaps in general are the most common style of implementation of priority queues. There are other, more
exotic types of heap than we cover here that can also be used - and that correspond to slightly different sorting
algorithms.)

There's not much to say - simply maintain an internal binary heap that you add and remove items to/from, and you should
see how this straightforwardly gives you $\mathrm{O}(log(n))$ `enqueue` and `dequeue`, and $\mathrm{O}(1)$ `front`.

If there are multiple items with the same priority, these will not necessarily be removed in FIFO order. This is
because, although heaps' adds newer items further down/right, their removal operations can cause them to change order.
This is reflected in heapsort not being a "stable" sort, in that equal items aren't necessarily left in the same order
post-sort as they were pre-sort.

You've the same three methods (`enqueue`, `front`, `dequeue`) to implement, but you should find that they can each be
implemented in one line each. So: three more lines, then you're done with the lab!
