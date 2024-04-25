"""
Data Structures & Algorithms

Lab 9: Binary Heaps & Priority Queues

Unsorted List Priority Queues Exercise
"""

from collections.abc import Iterator

from lib.base import Base
from lib.errors import EmptyCollectionError
from lib.type_vars import Priority, Item

from lab3.core.dynamic_array_list import DynamicArrayList


class UnsortedListPriorityQueue(Base[Priority, Item]):
    """
    A priority queue implemented using an unsorted list.

    Space: O(self.get_length())
    """

    _items: DynamicArrayList[tuple[Priority, Item]]
    _is_max: bool

    def __init__(self, is_max: bool = True) -> None:
        """
        Initialize this unsorted list priority queue.

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
    ) -> "UnsortedListPriorityQueue[Priority, Item]":
        """
        Build an unsorted list priority queue containing the given items.

        +--------+------------------+
        | Time:  | O(length(items)) |
        +--------+------------------+
        | Space: | O(1)             |
        +--------+------------------+

        :parameter items: an iterator of initial items
        :parameter is_max: ``True`` if it should be a max-queue, ``False`` if a min-queue (default ``True``)
        :returns: an unsorted list priority queue of those items
        """
        priority_queue = UnsortedListPriorityQueue(is_max=is_max)
        priority_queue._items = DynamicArrayList.build(items)
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

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+
        """
        self._items.insert_last((priority, item))

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
        if self.is_empty():
            raise EmptyCollectionError
        item = self._items.get_at(0)
        for i in range(1, self.get_length()):
            new_item = self._items.get_at(i)
            if self._is_higher_priority(new_item[0], item[0]):
                item = new_item
        return item

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
        if self.is_empty():
            raise EmptyCollectionError
        index = 0
        item = self._items.get_at(0)[0]
        for i in range(1, self.get_length()):
            new_item = self._items.get_at(i)[0]
            if self._is_higher_priority(new_item, item):
                index, item = i, new_item
        return self._items.remove_at(index)

    def _is_higher_priority(self, a: Priority, b: Priority) -> bool:
        if self._is_max:
            return a > b
        else:
            return a < b

    def iterator(self) -> Iterator[tuple[Priority, Item]]:
        priority_queue = UnsortedListPriorityQueue.build(self._items.iterator(), is_max=self._is_max)
        while not priority_queue.is_empty():
            yield priority_queue.dequeue()
