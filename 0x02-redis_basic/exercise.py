#!/usr/bin/env python3
"""This module contains a basic exercise using redis"""
import redis
import uuid
from typing import Union


class Cache:
    """A class for caching"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Returns a string"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key
