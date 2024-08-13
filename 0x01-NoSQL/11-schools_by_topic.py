#!/usr/bin/env python3
"""
return list of school having specific
topic
"""
# Python function that returns the list of school having a specific topic:

# Prototype: def schools_by_topic(mongo_collection, topic):
# mongo_collection will be the pymongo collection object
# topic (string) will be topic searched


def schools_by_topic(mongo_collection, topic) -> list:
    """returns a list of schools having a specific topic
    Args:
        mango_collection: Collection -> pymongo collection object
        topic: str -> topic to be queried

    Returns:
        list: List of schools having the specific topic
    """
    return list(mongo_collection.find(
        {'topics': topic}
    ))
