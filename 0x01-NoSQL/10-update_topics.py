#!/usr/bin/env python3
"""
This module defines a function that changes all topics of a school document
based on the name
"""


def update_topics(mongo_collection, name, topics):
    """Updates topics for a school document based on the name.
    Args:
        mongo_collection: The PyMongo collection object.
        name: The school name to update.
       topics:  
       A list of topics to be updated.
    Returns:
       The number of documents updated.
  """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
