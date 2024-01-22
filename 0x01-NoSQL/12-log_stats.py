#!/usr/bin/env python3
"""
A Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

def nginx_logs():
    """Provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient("mongodb://localhost:27017")
    nginx_collection = client.logs.nginx

    tot_count = nginx_collection.count_documents({})
    print(f"{tot_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for meth in methods:
        count = nginx_collection.count_documents({"method": meth})
        print(f"\tmethod {meth}: {count}")

    status = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    nginx_logs()
