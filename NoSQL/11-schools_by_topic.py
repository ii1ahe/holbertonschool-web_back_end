#!/usr/bin/env python3

"""
This module provides a function to find all schools that cover a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Finds all school documents where the 'topics' array contains the given topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic string to search for

    Returns:
        List of matching school documents.
    """
    return list(mongo_collection.find({"topics": topic}))
