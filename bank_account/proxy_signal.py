from typing import Callable

from .bank_account_protocol import BankAccountProtocol


Signal = Callable[[BankAccountProtocol, int], None] | None


class ProxySignalContextManager:
    def __init__(self,
                 bank_account: BankAccountProtocol,
                 value: int,
                 pre_signal: Signal = None,
                 post_signal: Signal = None):
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


class ProxySignal:
    def __init__(self,
                 bank_account: BankAccountProtocol,
                 pre_add: Signal = None,
                 post_add: Signal = None,
                 pre_sub: Signal = None,
                 post_sub: Signal = None,
                 ):
        self._bank_account = bank_account
        self._pre_add = pre_add
        self._post_add = post_add
        self._pre_sub = pre_sub
        self._post_sub = post_sub

    @property
    def amount(self) -> int:
        return self._bank_account.amount

    @amount.setter
    def amount(self, value: int) -> None:
        self._bank_account.amount = value

    def add(self, value: int) -> None:
        with ProxySignalContextManager(self._bank_account, value, self._pre_add, self._post_add):
            self._bank_account.add(value)

    def sub(self, value: int) -> None:
        with ProxySignalContextManager(self._bank_account, value, self._pre_sub, self._post_sub):
            self._bank_account.sub(value)
