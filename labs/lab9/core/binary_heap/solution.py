"""
Data Structures & Algorithms

Lab 9: Binary Heaps & Priority Queues

Binary Heaps Solution
"""

from collections.abc import Iterator

from lib.base import Base
from lib.errors import EmptyCollectionError
from lib.type_vars import Key, Value

from lab3.core.dynamic_array_list import DynamicArrayList


class BinaryHeap(Base[Key, Value]):
    """
    A binary heap.

    Space: O(self.get_length())
    """

    _items: DynamicArrayList[tuple[Key, Value]]
    _is_max: bool

    def __init__(self, is_max: bool = True):
        """
        Initialize this binary heap.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter is_max: ``True`` if it should be a max-heap, ``False`` if a min-heap (default ``True``)
        """
        self._items = DynamicArrayList()
        self._is_max = is_max

    @staticmethod
    def build(items: Iterator[tuple[Key, Value]], is_max: bool = True) -> "BinaryHeap[Key, Value]":
        """
        Build a binary heap containing the given items.

        +--------+------------------+
        | Time:  | O(length(items)) |
        +--------+------------------+
        | Space: | O(length(items)) |
        +--------+------------------+

        :parameter items: an iterator of initial items
        :parameter is_max: ``True`` if it should be a max-heap, ``False`` if a min-heap (default ``True``)
        :returns: a binary heap of those items
        """
        heap = BinaryHeap(is_max=is_max)
        heap._items = DynamicArrayList.build(items)
        for index in reversed(range(heap._get_parent(heap.get_length() - 1) + 1)):
            heap._heapify_down(index)
        return heap

    def is_max(self) -> bool:
        """
        Check if this binary heap is a max-heap or a min-heap.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if it's a max-heap, else ``False``
        """
        return self._is_max

    def is_empty(self) -> bool:
        """
        Check if this binary heap is empty.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: ``True`` if it's empty, else ``False``
        """
        return self.get_length() == 0

    def get_length(self) -> int:
        """
        Get the number of items in this binary heap.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the length
        """
        return self._items.get_length()

    def get_root(self) -> tuple[Key, Value]:
        """
        Get the item at the root of this binary heap.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :returns: the maximum item if the heap is a max-heap, else the minimum item
        :raises EmptyCollectionError: if the heap is empty
        """
        return self._items.get_first()

    def insert(self, key: Key, value: Value) -> None:
        """
        Insert the given item into this binary heap.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :parameter key: the key
        :parameter value: the value
        """
        self._items.insert_last((key, value))
        self._heapify_up(self.get_length() - 1)

    def remove_root(self) -> tuple[Key, Value]:
        """
        Remove and return the item at the root of this binary heap.

        +--------+----------------------------+
        | Time:  | O(log2(self.get_length())) |
        +--------+----------------------------+
        | Space: | O(1)                       |
        +--------+----------------------------+

        :returns: what was the maximum (if the heap is a max-heap, else the minimum) item
        :raises EmptyCollectionError: if the heap is empty
        """
        if self.is_empty():
            raise EmptyCollectionError
        self._swap(0, self.get_length() - 1)
        item = self._items.remove_last()
        self._heapify_down(0)
        return item

    def _has_parent(self, index: int) -> bool:
        return self._get_parent(index) >= 0

    def _has_left(self, index: int) -> bool:
        return self._get_left(index) < self.get_length()

    def _has_right(self, index: int) -> bool:
        return self._get_right(index) < self.get_length()

    def _is_root(self, index: int) -> bool:
        return not self._has_parent(index)

    def _is_leaf(self, index: int) -> bool:
        return not self._has_left(index)

    def _get_parent(self, index: int) -> int:
        """
        Given an index, get the index representing its parent.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the child index
        :returns: the parent index
        """
        return (index - 1) // 2

    def _get_left(self, index: int) -> int:
        """
        Given an index, get the index representing its left child.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the parent index
        :returns: the left child index
        """
        return index * 2 + 1

    def _get_right(self, index: int) -> int:
        """
        Given an index, get the index representing its right child.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter index: the parent index
        :returns: the right child index
        """
        return index * 2 + 2

    def _heapify_up(self, index: int) -> None:
        """
        Heapify up from the given index.

        +--------+-----------------+
        | Time:  | O(level(index)) |
        +--------+-----------------+
        | Space: | O(1)            |
        +--------+-----------------+

        :parameter array: the array of items
        :parameter index: the index to heapify up from
        """
        if self._has_parent(index):
            parent_index = self._get_parent(index)
            if self._has_greater_key(index, parent_index):
                self._swap(parent_index, index)
                self._heapify_up(parent_index)

    def _heapify_down(self, index: int) -> None:
        """
        Heapify down from the given index in the given array.

        +--------+------------------+
        | Time:  | O(height(index)) |
        +--------+------------------+
        | Space: | O(1)             |
        +--------+------------------+

        :parameter array: the array of items
        :parameter index: the index to heapify down from
        """
        if not self._has_left(index):
            return
        left_index = self._get_left(index)
        if self._has_right(index):
            right_index = self._get_right(index)
            if self._has_greater_key(left_index, right_index):
                child_index = left_index
            else:
                child_index = right_index
        else:
            child_index = left_index
        if self._has_greater_key(child_index, index):
            self._swap(child_index, index)
            self._heapify_down(child_index)

    def _has_greater_key(self, greater_index: int, lesser_index: int) -> bool:
        """
        Given two indices, check whether the key of the item at the first is greater than that of the second.

        Greater means greater if this is a max-heap, else it means lesser.

        +--------+------+
        | Time:  | O(1) |
        +--------+------+
        | Space: | O(1) |
        +--------+------+

        :parameter greater_index: the index which might have an item with a greater key
        :parameter lesser_index: the index which might have an item with a greater key
        :returns: ``True`` if TODO, else ``False``
        :raises IndexError: if either index is out of bounds TODO
        """
        lesser_key, _ = self._items.get_at(lesser_index)
        greater_key, _ = self._items.get_at(greater_index)
        if self._is_max:
            return greater_key > lesser_key
        else:
            return greater_key < lesser_key

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

    def iterator(self) -> Iterator[tuple[Key, Value]]:
        heap = BinaryHeap(is_max=self._is_max)
        heap._items = DynamicArrayList.build(self._items.iterator())
        while not heap.is_empty():
            yield heap.remove_root()
