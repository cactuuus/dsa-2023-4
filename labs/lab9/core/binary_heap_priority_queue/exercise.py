"""
Data Structures & Algorithms

Lab 9: Binary Heaps & Priority Queues

Binary Heap Priority Queues Exercise
"""

from collections.abc import Iterator

from lib.base import Base
from lib.type_vars import Priority, Item

from lab9.core.binary_heap import BinaryHeap


class BinaryHeapPriorityQueue(Base[Priority, Item]):
    """
    A priority queue implemented using a binary heap.

    Space: O(self.get_length())
    """

    _items: BinaryHeap[Priority, Item]

    def __init__(self, is_max: bool = True) -> None:
        """
        Initialize this binary heap priority queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter is_max: ``True`` if it should be a max-queue, ``False`` if a min-queue (default ``True``)
        """
        self._items = BinaryHeap(is_max=is_max)

    @staticmethod
    def build(items: Iterator[tuple[Priority, Item]], is_max: bool = True) -> "BinaryHeapPriorityQueue[Priority, Item]":
        """
        Build a binary heap priority queue containing the given items.

        +--------+----------------------------------------+
        | Time:  | O(length(items) * log2(length(items))) |
        +--------+----------------------------------------+
        | Space: | O(length(items))                       |
        +--------+----------------------------------------+

        :parameter items: an iterator of initial items
        :parameter is_max: ``True`` if it should be a max-queue, ``False`` if a min-queue (default ``True``)
        :returns: a binary heap priority queue of those items
        """
        priority_queue = BinaryHeapPriorityQueue(is_max=is_max)
        priority_queue._items = BinaryHeap.build(items)
        return priority_queue

    def is_max(self) -> bool:
        """
        Check if this priority queue is a max-queue or a min-queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if it's a max-queue, else ``False``
        """
        return self._items.is_max()

    def is_empty(self) -> bool:
        """
        Check if this priority queue is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if it's empty, else ``False``
        """
        return self._items.is_empty()

    def get_length(self) -> int:
        """
        Get the number of items in this priority queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return self._items.get_length()

    def enqueue(self, priority: Priority, item: Item) -> None:
        """
        Enqueue the given item with the given priority.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+
        """
        raise NotImplementedError

    def front(self) -> tuple[Priority, Item]:
        """
        Get the highest- (if it's a max-queue, else lowest-) priority item in this priority queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: a pair of the priority and item
        :raises EmptyCollectionError: if the priority queue is empty
        """
        raise NotImplementedError

    def dequeue(self) -> tuple[Priority, Item]:
        """
        Dequeue the highest- (if it's a max-queue, else lowest-) priority item in this priority queue.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: a pair of the priority and item
        :raises EmptyCollectionError: if the priority queue is empty
        """
        raise NotImplementedError
