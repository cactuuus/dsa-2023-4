"""
Data Structures & Algorithms

Lab 9: Binary Heaps & Priority Queues

Sorted List Priority Queues Exercise
"""

from collections.abc import Iterator

from lib.array import Array
from lib.base import Base
from lib.type_vars import Priority, Item

from lab3.core.dynamic_array_list import DynamicArrayList
from lab4.core.merge_sort import merge_sort


class SortedListPriorityQueue(Base[Priority, Item]):
    """
    A priority queue implemented using an sorted list.

    Space: O(self.get_length())
    """

    _items: DynamicArrayList[tuple[Priority, Item]]
    _is_max: bool

    def __init__(self, is_max: bool = True) -> None:
        """
        Initialize this sorted list priority queue.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter is_max: ``True`` if it should be a max-queue, ``False`` if a min-queue (default ``True``)
        """
        self._items = DynamicArrayList()
        self._is_max = is_max

    @staticmethod
    def build(
        items: Iterator[tuple[Priority, Item]],
        is_max: bool = True,
    ) -> "SortedListPriorityQueue[Priority, Item]":
        """
        Build an sorted list priority queue containing the given items.

        +--------+------------------+
        | Time:  | O(length(items)) |
        +--------+------------------+
        | Space: | O(1)             |
        +--------+------------------+

        :parameter items: an iterator of initial items
        :parameter is_max: ``True`` if it should be a max-queue, ``False`` if a min-queue (default ``True``)
        :returns: an sorted list priority queue of those items
        """
        priority_queue = SortedListPriorityQueue(is_max=is_max)
        sorted_items = Array.build(items)
        merge_sort(sorted_items)
        if is_max:
            priority_queue._items = DynamicArrayList.build(sorted_items.iterator())
        else:
            priority_queue._items = DynamicArrayList.build(sorted_items.reverse_iterator())
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
        return self._is_max

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

        +--------+----------------------+
        | Time:  | O(self.get_length()) |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+
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

        +--------+----------------------+
        | Time:  | O(1) amortized       |
        +--------+----------------------+
        | Space: | O(self.get_length()) |
        +--------+----------------------+

        :returns: a pair of the priority and item
        :raises EmptyCollectionError: if the priority queue is empty
        """
        raise NotImplementedError

    def _is_higher_priority(self, a: Priority, b: Priority) -> bool:
        if self._is_max:
            return a > b
        else:
            return a < b

    def _swap(self, index_a: int, index_b: int) -> None:
        """
        Swap the items at the given indices.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index_a: the index that should instead contain the item at ``index_b``
        :parameter index_b: the index that should instead contain the item at ``index_a``
        :raises IndexError: if ``index_a`` or ``index_b`` are out of bounds
        """
        temp = self._items.get_at(index_a)
        self._items.set_at(index_a, self._items.get_at(index_b))
        self._items.set_at(index_b, temp)

    def iterator(self) -> Iterator[tuple[Priority, Item]]:
        yield from self._items.reverse_iterator()
