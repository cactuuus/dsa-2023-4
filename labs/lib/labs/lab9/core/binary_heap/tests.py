from typing import Annotated

from lib.array import Array
from lib.errors import EmptyCollectionError
from lib.iterator import iterator
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Key, Value

from lab4.core.merge_sort import merge_sort
from lab9.core.binary_heap.exercise import BinaryHeap


@Test
def max_heapify_up_example_1():
    heap = BinaryHeap.build(
        iterator(
            (100, "a"),
            (75, "b"),
            (46, "c"),
            (15, "d"),
            (60, "e"),
            (30, "f"),
            (25, "g"),
            (7, "h"),
            (10, "i"),
            (90, "j"),
        )
    )
    index = heap.get_length() - 1
    heap._heapify_up(index)
    yield iterator(
        (100, "a"),
        (90, "j"),
        (46, "c"),
        (15, "d"),
        (75, "b"),
        (30, "f"),
        (25, "g"),
        (7, "h"),
        (10, "i"),
        (60, "e"),
    )
    yield heap._items.iterator()


@Test
def max_heapify_up_example_2():
    heap = BinaryHeap.build(
        iterator(
            (100, "a"),
            (75, "b"),
            (46, "c"),
            (15, "d"),
            (60, "e"),
            (30, "f"),
            (25, "g"),
            (7, "h"),
            (10, "i"),
            (0, "j"),
        )
    )
    index = heap.get_length() - 1
    heap._heapify_up(index)
    yield iterator(
        (100, "a"),
        (75, "b"),
        (46, "c"),
        (15, "d"),
        (60, "e"),
        (30, "f"),
        (25, "g"),
        (7, "h"),
        (10, "i"),
        (0, "j"),
    )
    yield heap._items.iterator()


@Test
def max_heapify_up_example_3():
    heap = BinaryHeap.build(
        iterator(
            (100, "a"),
            (75, "b"),
            (46, "c"),
            (15, "d"),
            (60, "e"),
            (30, "f"),
            (25, "g"),
            (7, "h"),
            (10, "i"),
            (60, "j"),
        )
    )
    index = heap.get_length() - 1
    heap._heapify_up(index)
    yield iterator(
        (100, "a"),
        (75, "b"),
        (46, "c"),
        (15, "d"),
        (60, "e"),
        (30, "f"),
        (25, "g"),
        (7, "h"),
        (10, "i"),
        (60, "j"),
    )
    yield heap._items.iterator()


@Test
def max_heapify_up_example_4():
    heap = BinaryHeap.build(
        iterator(
            (100, "a"),
            (75, "b"),
            (46, "c"),
            (15, "d"),
            (60, "e"),
            (30, "f"),
            (25, "g"),
            (7, "h"),
            (10, "i"),
            (120, "j"),
        )
    )
    index = heap.get_length() - 1
    heap._heapify_up(index)
    yield iterator(
        (120, "j"),
        (100, "a"),
        (46, "c"),
        (15, "d"),
        (75, "b"),
        (30, "f"),
        (25, "g"),
        (7, "h"),
        (10, "i"),
        (60, "e"),
    )
    yield heap._items.iterator()


@Test
def max_heapify_down_example_1():
    heap = BinaryHeap.build(
        iterator(
            (100, "a"),
            (75, "b"),
            (46, "c"),
            (15, "d"),
            (60, "e"),
            (30, "f"),
            (25, "g"),
            (7, "h"),
            (10, "i"),
        )
    )
    heap._heapify_down(0)
    yield iterator(
        (100, "a"),
        (75, "b"),
        (46, "c"),
        (15, "d"),
        (60, "e"),
        (30, "f"),
        (25, "g"),
        (7, "h"),
        (10, "i"),
    )
    yield heap._items.iterator()


@Test
def max_heapify_down_example_2():
    heap = BinaryHeap.build(
        iterator(
            (10, "a"),
            (75, "b"),
            (46, "c"),
            (15, "d"),
            (60, "e"),
            (30, "f"),
            (25, "g"),
            (7, "h"),
        )
    )
    heap._heapify_down(0)
    yield iterator(
        (75, "b"),
        (60, "e"),
        (46, "c"),
        (15, "d"),
        (10, "a"),
        (30, "f"),
        (25, "g"),
        (7, "h"),
    )
    yield heap._items.iterator()


@Test
def max_heapify_down_example_3():
    heap = BinaryHeap.build(
        iterator(
            (7, "a"),
            (75, "b"),
            (46, "c"),
            (15, "d"),
            (60, "e"),
            (30, "f"),
            (25, "g"),
        )
    )
    heap._heapify_down(0)
    yield iterator(
        (75, "b"),
        (60, "e"),
        (46, "c"),
        (15, "d"),
        (7, "a"),
        (30, "f"),
        (25, "g"),
    )
    yield heap._items.iterator()


# TODO: min_heapify_*


@Test
def max_insert_on_empty_then_get_length(
    key: Key,
    value: Value,
):
    heap = BinaryHeap()
    heap.insert(key, value)
    yield 1
    yield heap.get_length()


@Test
def min_insert_on_empty_then_get_length(
    key: Key,
    value: Value,
):
    heap = BinaryHeap(is_max=False)
    heap.insert(key, value)
    yield 1
    yield heap.get_length()


@Test
def max_insert_on_non_empty_then_get_length(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
    key: Key,
    value: Value,
):
    heap = BinaryHeap.build(items.iterator())
    heap.insert(key, value)
    yield items.get_length() + 1
    yield heap.get_length()


@Test
def min_insert_on_non_empty_then_get_length(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
    key: Key,
    value: Value,
):
    heap = BinaryHeap.build(items.iterator(), is_max=False)
    heap.insert(key, value)
    yield items.get_length() + 1
    yield heap.get_length()


@Test
def max_insert_all_on_empty_then_get_root(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap()
    root_key, root_value = items.get_at(0)
    for key, value in items.iterator():
        if key > root_key:
            root_key, root_value = key, value
        heap.insert(key, value)
    yield root_key, root_value
    yield heap.get_root()


@Test
def min_insert_all_on_empty_then_get_root(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap(is_max=False)
    root_key, root_value = items.get_at(0)
    for key, value in items.iterator():
        if key < root_key:
            root_key, root_value = key, value
        heap.insert(key, value)
    yield root_key, root_value
    yield heap.get_root()


@Test
def max_insert_all_on_non_empty_then_get_root(
    initial_items: Annotated[Array[tuple[Key, Value]], GE(1)],
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(initial_items.iterator())
    root_key, root_value = heap.get_root()
    for key, value in items.iterator():
        if key > root_key:
            root_key, root_value = key, value
        heap.insert(key, value)
    yield root_key, root_value
    yield heap.get_root()


@Test
def min_insert_all_on_non_empty_then_get_root(
    initial_items: Annotated[Array[tuple[Key, Value]], GE(1)],
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(initial_items.iterator(), is_max=False)
    root_key, root_value = heap.get_root()
    for key, value in items.iterator():
        if key < root_key:
            root_key, root_value = key, value
        heap.insert(key, value)
    yield root_key, root_value
    yield heap.get_root()


@Test
def max_insert_all_on_empty_then_remove_root(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap()
    root_key, root_value = items.get_at(0)
    for key, value in items.iterator():
        if key > root_key:
            root_key, root_value = key, value
        heap.insert(key, value)
    yield root_key, root_value
    yield heap.remove_root()


@Test
def min_insert_all_on_empty_then_remove_root(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap(is_max=False)
    root_key, root_value = items.get_at(0)
    for key, value in items.iterator():
        if key < root_key:
            root_key, root_value = key, value
        heap.insert(key, value)
    yield root_key, root_value
    yield heap.remove_root()


@Test
def max_insert_all_on_non_empty_then_remove_root(
    initial_items: Annotated[Array[tuple[Key, Value]], GE(1)],
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(initial_items.iterator())
    root_key, root_value = heap.get_root()
    for key, value in items.iterator():
        if key > root_key:
            root_key, root_value = key, value
        heap.insert(key, value)
    yield root_key, root_value
    yield heap.remove_root()


@Test
def min_insert_all_on_non_empty_then_remove_root(
    initial_items: Annotated[Array[tuple[Key, Value]], GE(1)],
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(initial_items.iterator(), is_max=False)
    root_key, root_value = heap.get_root()
    for key, value in items.iterator():
        if key < root_key:
            root_key, root_value = key, value
        heap.insert(key, value)
    yield root_key, root_value
    yield heap.remove_root()


@Test
def max_insert_all_on_empty_then_get_length(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap()
    for key, value in items.iterator():
        heap.insert(key, value)
    yield items.get_length()
    yield heap.get_length()


@Test
def min_insert_all_on_empty_then_get_length(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap(is_max=False)
    for key, value in items.iterator():
        heap.insert(key, value)
    yield items.get_length()
    yield heap.get_length()


@Test
def max_insert_all_on_non_empty_then_get_length(
    initial_items: Annotated[Array[tuple[Key, Value]], GE(1)],
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(initial_items.iterator())
    for key, value in items.iterator():
        heap.insert(key, value)
    yield initial_items.get_length() + items.get_length()
    yield heap.get_length()


@Test
def min_insert_all_on_non_empty_then_get_length(
    initial_items: Annotated[Array[tuple[Key, Value]], GE(1)],
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(initial_items.iterator(), is_max=False)
    for key, value in items.iterator():
        heap.insert(key, value)
    yield initial_items.get_length() + items.get_length()
    yield heap.get_length()


@Test
def max_get_root_on_empty():
    heap = BinaryHeap()
    yield EmptyCollectionError
    yield heap.get_root()


@Test
def min_get_root_on_empty():
    heap = BinaryHeap(is_max=False)
    yield EmptyCollectionError
    yield heap.get_root()


@Test
def max_get_root_on_non_empty(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    sorted_items = Array.build(items.iterator())
    merge_sort(sorted_items)
    heap = BinaryHeap.build(items.iterator())
    expect_key, _ = sorted_items.get_at(sorted_items.get_length() - 1)
    actual_key, _ = heap.get_root()
    yield expect_key
    yield actual_key


@Test
def min_get_root_on_non_empty(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    sorted_items = Array.build(items.iterator())
    merge_sort(sorted_items)
    heap = BinaryHeap.build(items.iterator(), is_max=False)
    expect_key, _ = sorted_items.get_at(0)
    actual_key, _ = heap.get_root()
    yield expect_key
    yield actual_key


@Test
def max_get_root_on_non_empty_then_get_length(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(items.iterator())
    length = heap.get_length()
    heap.get_root()
    yield length
    yield heap.get_length()


@Test
def min_get_root_on_non_empty_then_get_length(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(items.iterator(), is_max=False)
    length = heap.get_length()
    heap.get_root()
    yield length
    yield heap.get_length()


@Test
def max_remove_root_on_empty():
    heap = BinaryHeap()
    yield EmptyCollectionError
    yield heap.remove_root()


@Test
def min_remove_root_on_empty():
    heap = BinaryHeap(is_max=False)
    yield EmptyCollectionError
    yield heap.remove_root()


@Test
def max_remove_root_on_non_empty(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    sorted_items = Array.build(items.iterator())
    merge_sort(sorted_items)
    heap = BinaryHeap.build(items.iterator())
    expect_key, _ = sorted_items.get_at(sorted_items.get_length() - 1)
    actual_key, _ = heap.remove_root()
    yield expect_key
    yield actual_key


@Test
def min_remove_root_on_non_empty(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    sorted_items = Array.build(items.iterator())
    merge_sort(sorted_items)
    heap = BinaryHeap.build(items.iterator(), is_max=False)
    expect_key, _ = sorted_items.get_at(0)
    actual_key, _ = heap.remove_root()
    yield expect_key
    yield actual_key


@Test
def max_remove_root_on_non_empty_then_get_length(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(items.iterator())
    length = heap.get_length() - 1
    heap.remove_root()
    yield length
    yield heap.get_length()


@Test
def min_remove_root_on_non_empty_then_get_length(
    items: Annotated[Array[tuple[Key, Value]], GE(1)],
):
    heap = BinaryHeap.build(items.iterator(), is_max=False)
    length = heap.get_length() - 1
    heap.remove_root()
    yield length
    yield heap.get_length()


# TODO
