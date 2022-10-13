from abc import ABC
from abc import abstractmethod


class BankAccountABC(ABC):
    @property
    @abstractmethod
    def amount(self) -> int:
        ...

    @abstractmethod
    def add(self, value: int) -> None:
        ...

    @abstractmethod
    def sub(self, value: int) -> None:
        ...


class BankAccount(BankAccountABC):
    def __init__(self, username: str):
        self.username: str = username
        self._amount: int = 0

    @property
    def amount(self) -> int:
        return self._amount

    def add(self, value: int) -> None:
        if value <= 0:
            raise ValueError

        self._amount += value

    def sub(self, value: int) -> None:
        if value <= 0:
            raise ValueError
        if self._amount - value < 0:
            raise ValueError

        self._amount -= value
