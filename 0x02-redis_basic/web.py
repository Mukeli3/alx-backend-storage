#!/usr/bin/env python3
"""
"""
import requests
import redis
from functools import wraps


r = redis.Redis()


def counter(method):
    """
    """
    @wraps(method)
    def wrapper(url):
        cach_key = "cached:" + url
        cach_data = r.get(cach_key)
        if cach_data:
            return cach_data.decode("utf-8")

        key_count = "count:" + url
        html = method(url)

        r.incr(key_count)
        r.set(cach_key, html)
        r.expire(cach_key, 10)
        return html
    return wrapper


@counter
def get_page(url: str) -> str:
    """
    """
    return requests.get(url).text
