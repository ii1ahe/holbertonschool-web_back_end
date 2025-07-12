// my comment
#!/usr/bin/env python3

"""
This module lists all documents in the 'school' collection of a given MongoDB database.
"""

from pymongo import MongoClient
import sys

def list_school_documents(db_name):
    """
    Prints all documents from the 'school' collection in the given database.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client[db_name]
    documents = db.school.find()
    for doc in documents:
        print(doc)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-all.py <database_name>")
        sys.exit(1)
    list_school_documents(sys.argv[1])
