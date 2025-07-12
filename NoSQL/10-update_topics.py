#!/usr/bin/env python3

"""
This module provides a function to update the 'topics' of a school document by name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all documents where name == given name.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list of str): list of new topics
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
