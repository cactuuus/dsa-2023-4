from typing import Annotated

from lib.array import Array
from lib.errors import EmptyCollectionError
from lib.test import Test
from lib.test.annotations import *
from lib.type_vars import Item, Priority

from lab4.core.merge_sort import merge_sort
from lab9.core.unsorted_list_priority_queue.exercise import UnsortedListPriorityQueue


@Test
def max_enqueue_on_empty(
    priority: Priority,
    item: Item,
):
    priority_queue = UnsortedListPriorityQueue()
    priority_queue.enqueue(priority, item)
    yield priority, item
    yield priority_queue._items.get_at(0)


@Test
def min_enqueue_on_empty(
    priority: Priority,
    item: Item,
):
    priority_queue = UnsortedListPriorityQueue(is_max=False)
    priority_queue.enqueue(priority, item)
    yield priority, item
    yield priority_queue._items.get_at(0)


@Test
def max_enqueue_on_empty_then_get_length(
    priority: Priority,
    item: Item,
):
    priority_queue = UnsortedListPriorityQueue()
    priority_queue.enqueue(priority, item)
    yield 1
    yield priority_queue.get_length()


@Test
def min_enqueue_on_empty_then_get_length(
    priority: Priority,
    item: Item,
):
    priority_queue = UnsortedListPriorityQueue(is_max=False)
    priority_queue.enqueue(priority, item)
    yield 1
    yield priority_queue.get_length()


@Test
def max_enqueue_on_non_empty(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    priority: Priority,
    item: Item,
):
    priority_queue = UnsortedListPriorityQueue.build(items.iterator())
    priority_queue.enqueue(priority, item)
    yield priority, item
    yield priority_queue._items.get_at(priority_queue.get_length() - 1)


@Test
def min_enqueue_on_non_empty(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    priority: Priority,
    item: Item,
):
    priority_queue = UnsortedListPriorityQueue.build(items.iterator(), is_max=False)
    priority_queue.enqueue(priority, item)
    yield priority, item
    yield priority_queue._items.get_at(priority_queue.get_length() - 1)


@Test
def max_enqueue_on_non_empty_then_get_length(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    priority: Priority,
    item: Item,
):
    priority_queue = UnsortedListPriorityQueue.build(items.iterator())
    length = priority_queue.get_length() + 1
    priority_queue.enqueue(priority, item)
    yield length
    yield priority_queue.get_length()


@Test
def min_enqueue_on_non_empty_then_get_length(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    priority: Priority,
    item: Item,
):
    priority_queue = UnsortedListPriorityQueue.build(items.iterator(), is_max=False)
    length = priority_queue.get_length() + 1
    priority_queue.enqueue(priority, item)
    yield length
    yield priority_queue.get_length()


@Test
def max_enqueue_all_on_empty(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue()
    for priority, item in items.iterator():
        priority_queue.enqueue(priority, item)
    yield items.iterator()
    yield priority_queue._items.iterator()


@Test
def min_enqueue_all_on_empty(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue(is_max=False)
    for priority, item in items.iterator():
        priority_queue.enqueue(priority, item)
    yield items.iterator()
    yield priority_queue._items.iterator()


@Test
def max_enqueue_all_on_empty_then_front(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue()
    front_priority, front_item = items.get_at(0)
    for priority, item in items.iterator():
        if priority > front_priority:
            front_priority, front_item = priority, item
        priority_queue.enqueue(priority, item)
    yield front_priority, front_item
    yield priority_queue.front()


@Test
def min_enqueue_all_on_empty_then_front(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue(is_max=False)
    front_priority, front_item = items.get_at(0)
    for priority, item in items.iterator():
        if priority < front_priority:
            front_priority, front_item = priority, item
        priority_queue.enqueue(priority, item)
    yield front_priority, front_item
    yield priority_queue.front()


@Test
def max_enqueue_all_on_non_empty_then_front(
    initial_items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue.build(initial_items.iterator())
    front_priority, front_item = priority_queue.front()
    for priority, item in items.iterator():
        if priority > front_priority:
            front_priority, front_item = priority, item
        priority_queue.enqueue(priority, item)
    yield front_priority, front_item
    yield priority_queue.front()


@Test
def min_enqueue_all_on_non_empty_then_front(
    initial_items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue.build(initial_items.iterator(), is_max=False)
    front_priority, front_item = priority_queue.front()
    for priority, item in items.iterator():
        if priority < front_priority:
            front_priority, front_item = priority, item
        priority_queue.enqueue(priority, item)
    yield front_priority, front_item
    yield priority_queue.front()


@Test
def max_enqueue_all_on_empty_then_dequeue(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue()
    front_priority, front_item = items.get_at(0)
    for priority, item in items.iterator():
        if priority > front_priority:
            front_priority, front_item = priority, item
        priority_queue.enqueue(priority, item)
    yield front_priority, front_item
    yield priority_queue.dequeue()


@Test
def min_enqueue_all_on_empty_then_dequeue(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue(is_max=False)
    front_priority, front_item = items.get_at(0)
    for priority, item in items.iterator():
        if priority < front_priority:
            front_priority, front_item = priority, item
        priority_queue.enqueue(priority, item)
    yield front_priority, front_item
    yield priority_queue.dequeue()


@Test
def max_enqueue_all_on_non_empty_then_dequeue(
    initial_items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue.build(initial_items.iterator())
    front_priority, front_item = priority_queue.front()
    for priority, item in items.iterator():
        if priority > front_priority:
            front_priority, front_item = priority, item
        priority_queue.enqueue(priority, item)
    yield front_priority, front_item
    yield priority_queue.dequeue()


@Test
def min_enqueue_all_on_non_empty_then_dequeue(
    initial_items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue.build(initial_items.iterator(), is_max=False)
    front_priority, front_item = priority_queue.front()
    for priority, item in items.iterator():
        if priority < front_priority:
            front_priority, front_item = priority, item
        priority_queue.enqueue(priority, item)
    yield front_priority, front_item
    yield priority_queue.dequeue()


@Test
def max_enqueue_all_on_empty_then_get_length(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue()
    for priority, item in items.iterator():
        priority_queue.enqueue(priority, item)
    yield items.get_length()
    yield priority_queue.get_length()


@Test
def min_enqueue_all_on_empty_then_get_length(
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue(is_max=False)
    for priority, item in items.iterator():
        priority_queue.enqueue(priority, item)
    yield items.get_length()
    yield priority_queue.get_length()


@Test
def max_enqueue_all_on_non_empty_then_get_length(
    initial_items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue.build(initial_items.iterator())
    for priority, item in items.iterator():
        priority_queue.enqueue(priority, item)
    yield initial_items.get_length() + items.get_length()
    yield priority_queue.get_length()


@Test
def min_enqueue_all_on_non_empty_then_get_length(
    initial_items: Annotated[Array[tuple[Priority, Item]], GE(1)],
    items: Annotated[Array[tuple[Priority, Item]], GE(1)],
):
    priority_queue = UnsortedListPriorityQueue.build(initial_items.iterator(), is_max=False)
    for priority, item in items.iterator():
        priority_queue.enqueue(priority, item)
    yield initial_items.get_length() + items.get_length()
    yield priority_queue.get_length()


@Test
def max_front_on_empty():
    priority_queue = UnsortedListPriorityQueue()
    yield EmptyCollectionError
    yield priority_queue.front()


@Test
def min_front_on_empty():
    priority_queue = UnsortedListPriorityQueue(is_max=False)
    yield EmptyCollectionError
    yield priority_queue.front()


@Test
def max_front_on_non_empty(items: Annotated[Array[tuple[Priority, Item]], GE(1)]):
    sorted_items = Array.build(items.iterator())
    merge_sort(sorted_items)
    priority_queue = UnsortedListPriorityQueue.build(items.iterator())
    expect_priority, _ = sorted_items.get_at(sorted_items.get_length() - 1)
    actual_priority, _ = priority_queue.front()
    yield expect_priority
    yield actual_priority


@Test
def min_front_on_non_empty(items: Annotated[Array[tuple[Priority, Item]], GE(1)]):
    sorted_items = Array.build(items.iterator())
    merge_sort(sorted_items)
    priority_queue = UnsortedListPriorityQueue.build(items.iterator(), is_max=False)
    expect_priority, _ = sorted_items.get_at(0)
    actual_priority, _ = priority_queue.front()
    yield expect_priority
    yield actual_priority


@Test
def max_front_on_non_empty_then_get_length(items: Annotated[Array[tuple[Priority, Item]], GE(1)]):
    priority_queue = UnsortedListPriorityQueue.build(items.iterator())
    length = priority_queue.get_length()
    priority_queue.front()
    yield length
    yield priority_queue.get_length()


@Test
def min_front_on_non_empty_then_get_length(items: Annotated[Array[tuple[Priority, Item]], GE(1)]):
    priority_queue = UnsortedListPriorityQueue.build(items.iterator(), is_max=False)
    length = priority_queue.get_length()
    priority_queue.front()
    yield length
    yield priority_queue.get_length()


@Test
def max_dequeue_on_empty():
    priority_queue = UnsortedListPriorityQueue()
    yield EmptyCollectionError
    yield priority_queue.dequeue()


@Test
def min_dequeue_on_empty():
    priority_queue = UnsortedListPriorityQueue(is_max=False)
    yield EmptyCollectionError
    yield priority_queue.dequeue()


@Test
def max_dequeue_on_non_empty(items: Annotated[Array[tuple[Priority, Item]], GE(1)]):
    sorted_items = Array.build(items.iterator())
    merge_sort(sorted_items)
    priority_queue = UnsortedListPriorityQueue.build(items.iterator())
    expect_priority, _ = sorted_items.get_at(sorted_items.get_length() - 1)
    actual_priority, _ = priority_queue.dequeue()
    yield expect_priority
    yield actual_priority


@Test
def min_dequeue_on_non_empty(items: Annotated[Array[tuple[Priority, Item]], GE(1)]):
    sorted_items = Array.build(items.iterator())
    merge_sort(sorted_items)
    priority_queue = UnsortedListPriorityQueue.build(items.iterator(), is_max=False)
    expect_priority, _ = sorted_items.get_at(0)
    actual_priority, _ = priority_queue.dequeue()
    yield expect_priority
    yield actual_priority


@Test
def max_dequeue_on_non_empty_then_get_length(items: Annotated[Array[tuple[Priority, Item]], GE(1)]):
    priority_queue = UnsortedListPriorityQueue.build(items.iterator())
    length = priority_queue.get_length() - 1
    priority_queue.dequeue()
    yield length
    yield priority_queue.get_length()


@Test
def min_dequeue_on_non_empty_then_get_length(items: Annotated[Array[tuple[Priority, Item]], GE(1)]):
    priority_queue = UnsortedListPriorityQueue.build(items.iterator(), is_max=False)
    length = priority_queue.get_length() - 1
    priority_queue.dequeue()
    yield length
    yield priority_queue.get_length()
