#!/usr/bin/env python3
"""
This module defines a counter decorator and a get_page method
The core of the function is very simple. It uses the requests module to
obtain the HTML content of a particular URL and returns it.
"""
import requests
import redis
from functools import wraps


r = redis.Redis()


def counter(method):
    """
    A decorator, adds counting and cachig functionality to the decorated
    function
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
    Fetches URL content using requests and returns it as a string
    """
    return requests.get(url).text
