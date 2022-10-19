from .positive_int import PositiveInt


class BankAccount:
    amount = PositiveInt()

    def __init__(self, username: str):
        self.username: str = username
        self.amount = 0

    def add(self, value: int) -> None:
        self.amount += value

    def sub(self, value: int) -> None:
        self.amount -= value
