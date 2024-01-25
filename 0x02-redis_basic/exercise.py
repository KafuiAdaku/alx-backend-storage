#!/usr/bin/env python3
"""This module contains a basic exercise using redis"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps



def count_calls(method: Callable) -> Callable:
    """My decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """A class for caching"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Returns a string"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key, fn: Callable = None):
        """Gets a key"""
        if fn is None:
            return self._redis.get(key)
        return fn(self._redis.get(key))

    def get_str(self, key):
        """Gets a string"""
        return self.get(key, fn)

    def get_int(self, key):
        """Gets an int"""
        return self.get(key, fn)
