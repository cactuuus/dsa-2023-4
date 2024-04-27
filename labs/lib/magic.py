from collections.abc import Callable, Generator, Iterable, Iterator
from copy import copy
from enum import Enum
from inspect import getclasstree
from types import NoneType
from typing import Any

from lib.type_vars import Item


def indent_line(line: str) -> str:
    if line == "":
        return ""
    return "    " + line


def indented(s: str) -> str:
    return "\n".join(map(indent_line, s.split("\n")))


def indent_lines(lines: Iterable[str]) -> str:
    return indented("\n".join(lines))


def prepend_newline_unless_empty(s: str) -> str:
    if s == "":
        return ""
    return "\n" + s


def to_type_name(thing: Any) -> str:
    if isinstance(thing, Iterator):
        return "Iterator"
    return type(thing).__name__


def needs_no_id(thing):
    thing_type = type(thing)
    if thing_type is NoneType:
        return True
    if thing_type is bool:
        return True
    if thing_type is int:
        return True
    if thing_type is float:
        return True
    if thing_type is str:
        return True
    if thing_type is type:
        return True
    if thing_type is tuple:
        return True
    if issubclass(thing_type, Exception):
        return True
    if issubclass(thing_type, Iterator):
        return True
    if issubclass(thing_type, Enum):
        return True
    if thing_type.__name__ == "Array":
        return True
    if thing_type.__name__.endswith("Token"):
        return True
    if thing_type.__name__ == "Edge":
        return True
    # TODO: more
    return False


def is_shallow(thing):
    thing_type = type(thing)
    if thing_type is NoneType:
        return True
    if thing_type is bool:
        return True
    if thing_type is int:
        return True
    if thing_type is float:
        return True
    if thing_type is str:
        return True
    if issubclass(thing_type, Exception):
        return True
    if issubclass(thing_type, Iterator):
        return True
    if issubclass(thing_type, Enum):
        return True
    if thing_type.__name__.endswith("Token"):
        return True
    # TODO: more
    return False


def to_type_string(thing: Any) -> str:
    type_name = to_type_name(thing)
    if needs_no_id(thing):
        return type_name
    return f"{type_name}@{hex(id(thing))}"


def to_shallow_string(thing: Any) -> str:
    return to_string(thing) if is_shallow(thing) else "..."


def to_typed_shallow_string(thing: Any) -> str:
    return f"{to_type_string(thing)}{{{to_shallow_string(thing)}}}"


def mappings_to_string(mappings: Iterable[tuple[str, str]]) -> str:
    return prepend_newline_unless_empty(indent_lines(f"{key} = {value}" for key, value in mappings))


def members_to_string(thing: Any, *members: str) -> str:
    return mappings_to_string((member, to_typed_string(getattr(thing, member))) for member in members)


def to_repr(thing: Any) -> str:
    if hasattr(thing, "iterator") and callable(thing.iterator):
        return f"{type(thing).__name__}.build({to_repr(iter(list(thing.iterator())))})"
    if isinstance(thing, Iterator):
        if isinstance(thing, Generator):
            items = "..."
        else:
            items = ", ".join(to_repr(item) for item in copy(thing))
        return f"iterator({items})"
    return repr(thing)


def is_in(thing: Item, things: Iterable[Item]) -> bool:
    for thing_ in things:
        if thing is thing_:
            return True
    return False


def binary_subtree_to_string(subtree) -> str:
    if subtree is None:
        return ""
    item = to_string(subtree.get_item())
    if subtree.is_leaf():
        return item
    left = binary_subtree_to_string(subtree.get_left())
    right = binary_subtree_to_string(subtree.get_right())
    return f"({left}) {item} ({right})"


# noinspection PyProtectedMember
def to_string(thing: Any) -> str:
    match type(thing).__name__:
        case "Player":
            return members_to_string(thing, "_xp", "_position")
        case "Log":
            return "".join("\n" + item for item in thing.iterator())
        case "LogItem":
            return members_to_string(thing, "_time", "_level", "_message")
        case "SinglyLinkedList" | "DoublyLinkedList":
            visited_nodes = []
            node_strings = []
            for node in thing.nodes_iterator():
                node_strings.append(to_typed_string(node))
                if is_in(node, visited_nodes):
                    node_strings.append("...")
                    break
                visited_nodes.append(node)
            nodes = prepend_newline_unless_empty(indent_lines(node_strings))
            return mappings_to_string(
                {
                    "length": to_typed_string(thing._length),
                    "first_node": to_typed_shallow_string(thing._first_node),
                    "last_node": to_typed_shallow_string(thing._last_node),
                    "nodes": nodes,
                }.items()
            )
        case "SinglyLinkedNode":
            return mappings_to_string(
                {
                    "list": to_typed_shallow_string(thing._list),
                    "item": to_typed_string(thing._item),
                    "next_node": to_typed_shallow_string(thing._next_node),
                }.items()
            )
        case "DoublyLinkedNode":
            return mappings_to_string(
                {
                    "list": to_typed_shallow_string(thing._list),
                    "previous_node": to_typed_shallow_string(thing._previous_node),
                    "item": to_typed_string(thing._item),
                    "next_node": to_typed_shallow_string(thing._next_node),
                }.items()
            )
        case "Parenthesis":
            match thing.name:
                case "OPENING":
                    return "("
                case "CLOSING":
                    return ")"
            assert False
        case "Operator":
            match thing.name:
                case "ADDITION":
                    return "+"
                case "SUBTRACTION":
                    return "-"
                case "MULTIPLICATION":
                    return "*"
                case "DIVISION":
                    return "/"
                case "MODULO":
                    return "%"
                case "EXPONENTIATION":
                    return "^"
            assert False
        case "ValueToken":
            return to_string(thing.value)
        case "FunctionToken":
            return to_string(thing.name)
        case "OperatorToken":
            return to_string(thing.operator)
        case "ParenthesisToken":
            return to_string(thing.parenthesis)
        case "CommaToken":
            return ""
        case "HashFunction":
            return members_to_string(thing, "_a", "_b", "_size")
        case "BinaryTree":
            return to_string(thing._root) if thing._root else ""
        case "BinarySubtree":
            return binary_subtree_to_string(thing)
        case "Vertex":
            return to_string(thing._item) if thing._item is not None else ""
        case "Edge":
            s = thing._source
            t = thing._target
            i = thing._item
            if i is None:
                return f"{s} -> {t}"
            return f"{s} -[{i}]-> {t}"
    if isinstance(thing, Enum):
        return thing.name.title().replace("_", " ")
    if hasattr(thing, "iterator") and isinstance(thing.iterator, Callable):
        return ", ".join(map(to_typed_string, thing.iterator()))
    if isinstance(thing, str):
        return repr(thing)
    if isinstance(thing, Iterator) and not isinstance(thing, Generator):
        return ", ".join(map(to_typed_string, copy(thing)))
    match thing:
        case tuple() | list() | set():
            return ", ".join(map(to_typed_string, thing))
    if isinstance(thing, Iterable):
        return "..."
        # return ", ".join(map(to_typed_string, thing))
    return str(thing)


def to_typed_string(thing: Any) -> str:
    return f"{to_type_string(thing)}{{{to_string(thing)}}}"


def members_are_equal(thing_a: Any, thing_b: Any, *members: str) -> bool:
    for member in members:
        member_a = getattr(thing_a, member)
        member_b = getattr(thing_b, member)
        if not are_equal(member_a, member_b):
            return False
    return True


def get_super(subtype: type) -> type:
    return getclasstree([subtype])[0][0]


def is_base(t: type) -> bool:
    if t.__name__ == "Base":
        return True
    if t.__name__ == "object":
        return False
    return is_base(get_super(t))


def less_or_equal(thing_a: Any, thing_b: Any) -> bool:
    if not is_base(type(thing_a)):
        return thing_a <= thing_b
    if type(thing_a) is type(thing_b):
        match type(thing_a).__name__:
            case "Array":
                return list(thing_a.iterator()) <= list(thing_b.iterator())
            case "Vertex":
                if thing_a.get_item() != thing_b.get_item():
                    return thing_a.get_item() <= thing_b.get_item()
                return id(thing_a) <= id(thing_b)
            case "Edge":
                if thing_a._source is thing_b._source:
                    return less_or_equal(thing_a._target, thing_b._target)
                return less_or_equal(thing_a._source, thing_b._source)
    return NotImplemented


def are_equal(thing_a: Any, thing_b: Any) -> bool:
    if isinstance(thing_a, Iterator):
        if not isinstance(thing_b, Iterator):
            return False
        if not isinstance(thing_a, Generator):
            thing_a = copy(thing_a)
        # if not isinstance(thing_b, Generator):
        #     thing_b = copy(thing_b)
        try:
            return all(are_equal(a, b) for a, b in zip(thing_a, thing_b, strict=True))
        except ValueError:
            return False
    if type(thing_a) is not type(thing_b):
        return False
    if isinstance(thing_a, Enum):
        return thing_a.value == thing_b.value
    match type(thing_a).__name__:
        case "Player":
            return members_are_equal(thing_a, thing_b, "_xp", "_position")
        case "Pair":
            return members_are_equal(thing_a, thing_b, "_first", "_second")
        case "Log":
            return members_are_equal(thing_a, thing_b, "_log")
        case "LogItem":
            return members_are_equal(thing_a, thing_b, "_time", "_level", "_message")
        case "SinglyLinkedNode" | "DoublyLinkedNode":
            return thing_a is thing_b
            # return members_are_equal(thing_a, thing_b, "item")
        case "ValueToken":
            return members_are_equal(thing_a, thing_b, "_value")
        case "FunctionToken":
            return members_are_equal(thing_a, thing_b, "_name")
        case "OperatorToken":
            return members_are_equal(thing_a, thing_b, "_operator")
        case "ParenthesisToken":
            return members_are_equal(thing_a, thing_b, "_parenthesis")
        case "CommaToken":
            return True
        case "HashFunction":
            return members_are_equal(thing_a, thing_b, "_a", "_b", "_size")
        case "BinaryTree":
            return members_are_equal(thing_a, thing_b, "_root")
        case "BinarySubtree":
            return thing_a is thing_b
        case "Vertex":
            return thing_a is thing_b
        case "Edge":
            return members_are_equal(thing_a, thing_b, "_source", "_target")
    # if isinstance(thing_a, Iterable):
    #     return are_equal(iter(thing_a), iter(thing_b))
    if hasattr(thing_a, "iterator") and isinstance(thing_a.iterator, Callable):
        return are_equal(thing_a.iterator(), thing_b.iterator())
    return thing_a == thing_b
