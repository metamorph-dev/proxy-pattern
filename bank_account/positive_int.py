from typing import Any


class PositiveInt:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance: Any, owner=None):
        return getattr(instance, self.private_name, 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('The value can\'t be negative')

        setattr(instance, self.private_name, value)
