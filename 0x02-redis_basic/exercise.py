#!/usr/bin/env python3
"""
This module defines a class Cache
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        method stores an instance of the Redis client as a private variable
        """
        self.redis = redis.Redis()
        self._redis.flushdb()  # clear the Redis database

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method takes an argument and returns a string, generates a random key
        """
        key = str(uui.uuid4())  # generate a random key
        self._redis.set(key, data)  # store data in Redis
        return key  # return key
