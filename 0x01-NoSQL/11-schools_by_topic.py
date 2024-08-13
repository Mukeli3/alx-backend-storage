#!/usr/bin/env python3
"""
This module defines a function that returns the list of school having a
specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools with a specific topic.

  Args:
    mongo_collection: The PyMongo collection object.
    topic: The topic to search for.

  Returns:
    A list of school names.
    """
    return list(mongo_collection.find({"topics": topic})
