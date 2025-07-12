// my comment
#!/usr/bin/env python3

"""
This module lists all documents in the 'school' collection where name == 'Holberton school'.
"""

from pymongo import MongoClient
import sys

def list_matching_documents(db_name):
    """
    Prints documents from 'school' collection where name is 'Holberton school'.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client[db_name]
    documents = db.school.find({"name": "Holberton school"})
    for doc in documents:
        print(doc)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-match.py <database_name>")
        sys.exit(1)
    list_matching_documents(sys.argv[1])
