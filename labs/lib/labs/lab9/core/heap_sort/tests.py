from lib.array import Array
from lib.iterator import iterator
from lib.test import Test
from lib.type_vars import Item

from lab9.core.heap_sort.exercise import _max_heapify_up, _max_heapify_down, heap_sort


@Test
def max_heapify_up_example_1():
    array = Array.build(iterator(100, 75, 46, 15, 60, 30, 25, 7, 10, 90))
    index = array.get_length() - 1
    _max_heapify_up(array, index)
    yield Array.build(iterator(100, 90, 46, 15, 75, 30, 25, 7, 10, 60))
    yield array


@Test
def max_heapify_up_example_2():
    array = Array.build(iterator(100, 75, 46, 15, 60, 30, 25, 7, 10, 0))
    index = array.get_length() - 1
    _max_heapify_up(array, index)
    yield Array.build(iterator(100, 75, 46, 15, 60, 30, 25, 7, 10, 0))
    yield array


@Test
def max_heapify_up_example_3():
    array = Array.build(iterator(100, 75, 46, 15, 60, 30, 25, 7, 10, 60))
    index = array.get_length() - 1
    _max_heapify_up(array, index)
    yield Array.build(iterator(100, 75, 46, 15, 60, 30, 25, 7, 10, 60))
    yield array


@Test
def max_heapify_up_example_4():
    array = Array.build(iterator(100, 75, 46, 15, 60, 30, 25, 7, 10, 120))
    index = array.get_length() - 1
    _max_heapify_up(array, index)
    yield Array.build(iterator(120, 100, 46, 15, 75, 30, 25, 7, 10, 60))
    yield array


@Test
def max_heapify_down_example_1():
    array = Array.build(iterator(100, 75, 46, 15, 60, 30, 25, 7, 10))
    index = 0
    length = array.get_length() - 1
    _max_heapify_down(array, index, length)
    yield Array.build(iterator(100, 75, 46, 15, 60, 30, 25, 7, 10))
    yield array


@Test
def max_heapify_down_example_2():
    array = Array.build(iterator(10, 75, 46, 15, 60, 30, 25, 7, 100))
    index = 0
    length = array.get_length() - 1
    _max_heapify_down(array, index, length)
    yield Array.build(iterator(75, 60, 46, 15, 10, 30, 25, 7, 100))
    yield array


@Test
def max_heapify_down_example_3():
    array = Array.build(iterator(7, 75, 46, 15, 60, 30, 25, 100, 10))
    index = 0
    length = array.get_length() - 2
    _max_heapify_down(array, index, length)
    yield Array.build(iterator(75, 60, 46, 15, 7, 30, 25, 100, 10))
    yield array


@Test
def heap_sort_works(
    array: Array[Item],
):
    sorted_array = Array.build(iter(sorted(array.iterator())))
    heap_sort(array)
    yield sorted_array
    yield array
