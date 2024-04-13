# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 9: Binary Heaps & Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/README.md))

### [Unsorted List Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/unsorted_list_priority_queue/README.md)
```shell
python labs unsorted_list_priority_queue
```

We're now moving on to priority queues, which we're going to implement in four different ways.

First things first: Our priority queue interface is a little different to the lecture's, but only in its names for the
operations, not in their functionality. This is because we're going to be implementing priority queues that can, like
the binary heap we just implemented, be either max-queues or min-queues. Unlike binary heaps, priority queues don't
necessarily have a "root" to use as an agnostic term. What we're going to do instead is to simply reuse the names from
our queue interface:

| Lectures     | Labs      |
|--------------|-----------|
| `insert`     | `enqueue` |
| `find_max`   | `front`   |
| `remove_max` | `dequeue` |

(As always, it's not the names that matter, but the things themselves.)

This first priority queue works by using an unsorted list. It stores its items in a list, which it enqueues to by
simply appending, resulting in an unsorted list of items. This is, of course, very computationally cheap -
specifically, its `enqueue` should be $\mathrm{O}(1)$.

The downside comes when dequeueing. Since the items aren't all in order, it's not trivial to return the highest priority
item - first it be must be found, which can only be done by looking through the entire list, and is therefore
$\mathrm{O}(n)$. (Note that it's $\mathrm{O}(n)$ even in the best case - even if the highest priority item happens to be
the first item in the list, it must be compared against every other item in the list to be identified as the highest
priority item.)

This means that this is generally a pretty unpopular style of priority queue, as generally what matters is for
dequeueing to be fast, not enqueueing. (Sadly you can't have both be $\mathrm{O}(1)$. That said, it's possible to have
$\mathrm{O}(1)$ `enqueue` and $\mathrm{O}(1)$ `front`, but then `dequeue` can be no better than $\mathrm{O}(\log(n))$ -
anyway, none of the approaches we'll implement in the lab will be like that. In this case, for example, both `front` and
`dequeue` are $\mathrm{O}(n)$.)

Still, have a go at implementing it, and then we'll move on to other ways of building a priority queue.

---

Next:
- [Sorted List Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/sorted_list_priority_queue/README.md)
