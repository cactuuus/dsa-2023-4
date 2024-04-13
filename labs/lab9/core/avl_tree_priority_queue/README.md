# [Data Structures & Algorithms](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/README.md): [Labs](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/README.md)

## [Lab 9: Binary Heaps & Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/README.md) ([Core](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/README.md))

### [AVL Tree Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/avl_tree_priority_queue/README.md)
```shell
python labs avl_tree_priority_queue
```

Self-balancing BSTs are another way to implement the priority queue interface.

Given that we implemented an AVL tree in the previous lab, in this exercise we're going to use it to do just that.

Now, the way we implemented our AVL tree meant that it requires keys (which here will be priorities) to be unique. Of
course, in many situations we wouldn't want this restriction on a priority queue, but (a) in some cases it's not a
problem and (b) it is possible to implement AVL trees (and other types of self-balancing BSTs) in a way where this isn't
a restriction (though we're not covering that in this module).

Either way, BSTs are a less common way to implement priority queues than heaps (which is what we'll do in the next
exercise). Still, since we've got one laying around, we might as well use it!

(You should find that this is easier than the previous two exercises, as the AVL tree does most of the heavy lifting.)

---

Next:
- [Binary Heap Priority Queues](https://github.com/bertie-wheen/dsa-2023-4/blob/trunk/labs/lab9/core/binary_heap_priority_queue/README.md)
