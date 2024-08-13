#!/usr/bin/env python3
"""module: 9-insert_school
adds a document in a collection
"""
from pymongo.collection import Collection
from bson.objectid import ObjectId


def insert_school(mongo_collection: Collection, **kwargs) -> ObjectId:
    """Add a document to a collection.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        kwargs (dict): Dictionary for the document.

    Returns:
        ObjectId: The _id of the new mongo collection object.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
