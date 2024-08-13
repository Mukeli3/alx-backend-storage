#!/usr/bin/env python3
"""
This module defines a function that lists all documens in a collection
"""
import pymongo


def list_all(mongo_collection):
    docs = list(mongo_collection.find())
    return docs
