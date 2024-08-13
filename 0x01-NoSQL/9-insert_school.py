#!/usr/bin/env python3
"""module: 9-insert_school
adds a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """add a document to a collection
    Args:
        mongo_collection (Collection) -> mongo collection object
        kwargs (dict) -> dictionary for document
    Returns:
        ObjectId -> _id of the new mongo collection object
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
