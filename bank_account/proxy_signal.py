from typing import Callable

from .bank_account import BankAccountABC


class ProxySignalContextManager:
    def __init__(self,
                 bank_account: BankAccountABC,
                 value: int,
                 pre_signal: Callable[[BankAccountABC, int], None] | None = None,
                 post_signal: Callable[[BankAccountABC, int], None] | None = None):
        self._bank_account = bank_account
        self._value = value
        self._pre_signal = pre_signal
        self._post_signal = post_signal

    def __enter__(self):
        if self._pre_signal:
            self._pre_signal(self._bank_account, self._value)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None and self._post_signal:
            self._post_signal(self._bank_account, self._value)


class ProxySignal(BankAccountABC):
    def __init__(self,
                 bank_account: BankAccountABC,
                 pre_add: Callable[[BankAccountABC, int], None] | None = None,
                 post_add: Callable[[BankAccountABC, int], None] | None = None,
                 pre_sub: Callable[[BankAccountABC, int], None] | None = None,
                 post_sub: Callable[[BankAccountABC, int], None] | None = None,
                 ):
        self._bank_account = bank_account
        self._pre_add = pre_add
        self._post_add = post_add
        self._pre_sub = pre_sub
        self._post_sub = post_sub

    @property
    def amount(self) -> int:
        return self._bank_account.amount

    def add(self, value: int) -> None:
        with ProxySignalContextManager(self._bank_account, value, self._pre_add, self._post_add):
            self._bank_account.add(value)

    def sub(self, value: int) -> None:
        with ProxySignalContextManager(self._bank_account, value, self._pre_sub, self._post_sub):
            self._bank_account.sub(value)
