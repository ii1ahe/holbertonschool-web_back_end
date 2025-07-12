#!/usr/bin/env python3

"""
This module provides a function to list all documents from a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Returns all documents from the given MongoDB collection.
    If the collection is empty, returns an empty list.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        List of documents in the collection.
    """
    return list(mongo_collection.find())
