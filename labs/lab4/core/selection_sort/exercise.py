"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Selection Sort Exercise
"""

from lib.array import Array
from lib.type_vars import Item


def _swap(array: Array[Item], index_a: int, index_b: int) -> None:
    """
    Swap the items at the given indices in the given array.

    :parameter array: the array
    :parameter index_a: the index that should instead contain the item at ``index_b``
    :parameter index_b: the index that should instead contain the item at ``index_a``
    :raises IndexError: if ``index_a`` or ``index_b`` are out of bounds
    """
    a = array.get_at(index_a)
    b = array.get_at(index_b)
    array.set_at(index_a, b)
    array.set_at(index_b, a)


def selection_sort(array: Array[Item]) -> None:
    """
    Sort the given array in increasing order using selection sort.

    +--------+---------------------------+
    | Time:  | O(array.get_length() ^ 2) |
    +--------+---------------------------+
    | Space: | O(1)                      |
    +--------+---------------------------+

    :parameter array: the array to sort
    """
    for i in range(array.get_length()):
        min_index = i
        for j in range(i + 1, array.get_length()):
            if array.get_at(j) < array.get_at(min_index):
                min_index = j
        _swap(array, i, min_index)