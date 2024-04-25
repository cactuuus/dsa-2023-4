from typing import Any, Generic, Self, TypeVarTuple

from lib.magic import are_equal, less_or_equal, to_typed_string


TypeVars = TypeVarTuple("TypeVars")


class Base(Generic[*TypeVars]):
    def __str__(self) -> str:
        return to_typed_string(self)

    def __eq__(self, other: Any) -> bool:
        return are_equal(self, other)

    def __hash__(self) -> int:
        return hash(id(self))

    def __le__(self, other) -> bool:
        return less_or_equal(self, other)

    def __lt__(self, other) -> bool:
        ge = self >= other
        if ge is NotImplemented:
            return NotImplemented
        return not ge

    def __ge__(self, other) -> bool:
        return other <= self

    def __gt__(self, other) -> bool:
        le = self <= other
        if le is NotImplemented:
            return NotImplemented
        return not le

    def is_equal_to(self, other: Self) -> bool:
        return self is other
