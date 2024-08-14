#!/usr/bin/env python3
"""
This module defines a class Cache
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator counts calls to a method number
    """
    # create the key using the method's qualified name
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        function increments the count for a key everytime the method is called
        Return:
            function, value returned by the original method
        """
        self._redis.incr(key)  # increment the count in Redis
        return method(self, *args, **kwargs)

    return wrapper
class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        method stores an instance of the Redis client as a private variable
        """
        self._redis = redis.Redis()
        self._redis.flushdb()  # clear the Redis database

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method takes an argument and returns a string, generates a random key
        """
        key = str(uuid.uuid4())  # generate a random key
        self._redis.set(key, data)  # store data in Redis
        return key  # return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, None]:
        """
        method takes a key str arg and an optional Callable arg used o convert
        the data back to the desired format
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """ get a str value from Redis by key """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """ get an int value from Redis by key """
        return self.get(key, lambda x: int(x))
