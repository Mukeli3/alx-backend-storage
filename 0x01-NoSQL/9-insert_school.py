#!/usr/bin/env python3
"""
This module defines a function that inserts a new document in a collection
based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a PyMongo collection based on kwargs.

  Args:
    mongo_collection: The PyMongo collection object.
    kwargs: Keyword arguments to be inserted as document fields.

  Returns:
    The _id of the inserted document.
  """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
