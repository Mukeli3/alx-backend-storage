#!/usr/bin/env python3
"""
This module defines a function that provides some stats about Nginx logs
stored in Mongodb
Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT",
"PATCH", "DELETE"] in this order (see example below - warning: it’s a
tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
>> The purpose of this script is to quickly analyze Nginx logs to determine
the volume and type of requests handled by the server, which can be useful
for monitoring, debugging, or analyzing server traffic patterns.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    m_count = {}

    for method in methods:
        m_count[method] = collection.count_documents(
            {"method": method})

    query = {"path": "/status", "method": "GET"}
    status_docs = collection.count_documents(query)
    total = collection.count_documents({})

    print("{} logs".format(total))
    print("Methods:")
    for method, count in m_counts.items():
        print("\tmethod {}: {}".format(method, count))
    print("{} status check".format(status_docs))
