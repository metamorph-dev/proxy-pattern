from typing import Protocol

from .positive_int import PositiveInt


class BankAccountProtocol(Protocol):
    amount = PositiveInt()

    def add(self, value: int) -> None:
        ...

    def sub(self, value: int) -> None:
        ...
