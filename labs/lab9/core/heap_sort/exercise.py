"""
Data Structures & Algorithms

Lab 9: Binary Heaps & Priority Queues

Heap Sort Exercise
"""

from lib.array import Array
from lib.type_vars import Item


def _swap(array: Array[Item], index_a: int, index_b: int) -> None:
    """
    Swap the items at the given indices in the given array.

    +--------+------+
    | Time:  | O(1) |
    +--------+------+
    | Space: | O(1) |
    +--------+------+

    :parameter array: the array
    :parameter index_a: the index that should instead contain the item at ``index_b``
    :parameter index_b: the index that should instead contain the item at ``index_a``
    :raises IndexError: if ``index_a`` or ``index_b`` are out of bounds
    """
    a = array.get_at(index_a)
    b = array.get_at(index_b)
    array.set_at(index_a, b)
    array.set_at(index_b, a)


def _get_parent(index: int) -> int:
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


def _get_left(index: int) -> int:
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


def _get_right(index: int) -> int:
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


def _max_heapify_up(array: Array[Item], index: int) -> None:
    """
    Heapify up from the given index in the given array.

    +--------+-----------------+
    | Time:  | O(level(index)) |
    +--------+-----------------+
    | Space: | O(1)            |
    +--------+-----------------+

    :parameter array: the array of items
    :parameter index: the index to heapify up from
    """
    parent_index = _get_parent(index)
    if index == 0 or array.get_at(index) < array.get_at(parent_index):
        return
    _swap(array, index, parent_index)
    _max_heapify_up(array, parent_index)


def _max_heapify_down(array: Array[Item], index: int, length: int) -> None:
    """
    Heapify down from the given index in the given array.

    +--------+------------------+
    | Time:  | O(height(index)) |
    +--------+------------------+
    | Space: | O(1)             |
    +--------+------------------+

    :parameter array: the array of items
    :parameter index: the index to heapify down from
    :parameter length: the length of the heap (which is a prefix of the whole array)
    """
    left_index, right_index = _get_left(index), _get_right(index)
    if left_index >= length:
        return

    largest_child = left_index
    if right_index < length and array.get_at(left_index) < array.get_at(right_index):
        largest_child = right_index

    if array.get_at(index) < array.get_at(largest_child):
        _swap(array, index, largest_child)
        _max_heapify_down(array, largest_child, length)


def heap_sort(array: Array[Item]) -> None:
    """
    Sort the given array in increasing order using heap sort.

    +--------+--------------------------------------------------+
    | Time:  | O(array.get_length() * log2(array.get_length())) |
    +--------+--------------------------------------------------+
    | Space: | O(1)                                             |
    +--------+--------------------------------------------------+

    :parameter array: the array to sort
    """
    for index in range(1, array.get_length()):
        _max_heapify_up(array, index)
    for index in reversed(range(1, array.get_length())):
        _swap(array, 0, index)
        _max_heapify_down(array, 0, index)
