#!/usr/bin/env python3
"""
This module defines a function that returns all studens sorted by
average score
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of students sorted by average score with each student having
        an additional field 'averageScore'.
    """
    # Aggregation pipeline
    pipel = [
            {
                "$project": {
                    "name": "$name",  # Include the name field
                    "averageScore": { "$avg": "$topics.score" }
                    }
                },
            {
                "$sort": { "averageScore": -1 }  # Sort by average score in
                # descending order
                }
            ]

    # Execute the aggregation pipeline
    return list(mongo_collection.aggregate(pipel))
