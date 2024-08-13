#!/usr/bin/env python3
"""module 8-all
"""
from pymongo.collection import Collection
# Python function that lists all documents in a collection:

# Prototype: def list_all(mongo_collection):
# Return an empty list if no document in the collection
# mongo_collection will be the pymongo collection object


def list_all(mongo_collection: Collection) -> list:
    """list all documents in mongo_collection
    Args:
        mango_collection (Collection) -> pymongo collection
    Return:
        list: List of documents in collection
    """
    return list(mongo_collection.find())
