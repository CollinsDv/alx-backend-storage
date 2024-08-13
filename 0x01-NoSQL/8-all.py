#!/usr/bin/env python3
"""module 8-all
lists all documents in collection in python
"""
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> list:
    """list all documents in mongo_collection
    Args:
        mongo_collection (Collection) -> pymongo collection
    Returns:
        list: List of documents in collection
    """
    return mongo_collection.find()
