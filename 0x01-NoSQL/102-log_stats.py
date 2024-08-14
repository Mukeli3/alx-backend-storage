#!/usr/bin/env python3
"""
This module is an improvement of task 12, added the top 10 of the most
present IPs in the collection nginx of the database logs (The IPs are
sorted)
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

    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
        ])

    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))
