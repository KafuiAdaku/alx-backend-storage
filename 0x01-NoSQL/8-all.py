#!/usr/bin/env python3
"""A Python function that lists all documents in a collection"""
import pymongo

# if __name__ == "__main__":
def list_all(mongo_collection):
    """Lists all documents in a collection"""
    cursor_obj = mongo_collection.find()
    return list(cursor_obj)
