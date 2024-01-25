#!/usr/bin/env python3
"""This module contains a basic exercise using redis"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps



def count_calls(method: Callable) -> Callable:
    """Count decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """History decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


class Cache:
    """A class for caching"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        return self.get(key, str)

    def get_int(self, key):
        """Gets an int"""
        return self.get(key, int)


def replay(method: Callable):
    """Display history of calls of a particular functions"""
    r = redis.Redis()
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"
    inputs = r.lrange(input_key, 0, -1)
    outputs = r.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for input, output in zip(inputs, outputs):
        input = input.decode('utf-8') if input else ""
        output = output.decode('utf-8') if output else ""
        print(f"{method.__qualname__}(*{input}) -> {output}")
