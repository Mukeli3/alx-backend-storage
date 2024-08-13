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


def stats():
    """
    function provides Nginx logs stored in MongoDB statistics
    """
    client = MongoClient('mongodb://localhost:27017/') # connect to Mongodb
    db = client.logs  # database logs
    collection = db.nginx # nginx collection
    total = collection.count_documents({}) # total logs number
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        m_count[method] = collection.count_documents(
                {"method": method})

    s_checks = collection.count_documents({"method": "GET", "path": "/status"})

    # Display results
    print(f"{total} logs")
    print("Methods:")
    for method, count in m_count.items():
        print("\tmethod {}: {}".format(method, count))
    print(f"{s_checks} status checks")

if __name__ == "__main__":
    stats()
