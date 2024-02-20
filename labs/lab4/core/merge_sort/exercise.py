"""
Data Structures & Algorithms

Lab 4: Sorting & Array Maps

Merge Sort Exercise
"""

from lib.array import Array
from lib.type_vars import Item


def merge(array_a: Array[Item], array_b: Array[Item]) -> Array[Item]:
    """
    Merge the two sorted arrays into a single sorted array.

    +--------+------------------------------------------------+
    | Time:  | O(array_a.get_length() + array_b.get_length()) |
    +--------+------------------------------------------------+
    | Space: | O(array_a.get_length() + array_b.get_length()) |
    +--------+------------------------------------------------+

    :parameter array_a: a sorted array
    :parameter array_b: another sorted array
    :returns: a sorted array containing all the items in both the given arrays
    """
    length_a = array_a.get_length()
    length_b = array_b.get_length()
    sorted_array = Array(length_a + length_b)
    index_a, index_b = 0, 0
    for i in range(sorted_array.get_length()):
        item_a = array_a.get_at(index_a) if index_a < length_a else None
        item_b = array_b.get_at(index_b) if index_b < length_b else None
        if (item_a is not None and item_b is not None and item_a <= item_b) or item_b is None:
            sorted_array.set_at(i, item_a)
            index_a += 1
        else:
            sorted_array.set_at(i, item_b)
            index_b += 1
    return sorted_array


def merge_sort(array: Array[Item]) -> None:
    """
    Sort the given array in increasing order using merge sort.

    +--------+--------------------------------------------------+
    | Time:  | O(array.get_length() * log2(array.get_length())) |
    +--------+--------------------------------------------------+
    | Space: | O(array.get_length())                            |
    +--------+--------------------------------------------------+

    :parameter array: the array to sort
    """
    n = array.get_length()
    if n <= 1:
        return
    mid = n // 2
    left = Array(mid)
    right = Array(n - mid)
    for i in range(mid):
        left.set_at(i, array.get_at(i))
    for j in range(mid, n):
        right.set_at(j - mid, array.get_at(j))
    merge_sort(left)
    merge_sort(right)
    new_array = merge(left, right)
    for i in range(new_array.get_length()):
        array.set_at(i, new_array.get_at(i))
