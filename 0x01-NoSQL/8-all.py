#!/usr/bin/env python3
"""
This module defines a function that lists all documens in a collection
"""
import pymongo


def list_all(mongo_collection):
    """ lists all documents in a collection
    Args:
       mongo_collection: The PyMongo collection obj
    Returns:
       A list of docs or an empty list if no docs are found
    """
    docs = list(mongo_collection.find())
    return docs
