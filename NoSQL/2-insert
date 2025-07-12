// my comment
#!/usr/bin/env python3

"""
This module inserts a document into the 'school' collection of a specified MongoDB database.
"""

from pymongo import MongoClient
import sys

def insert_school_document(db_name):
    """
    Inserts a document with 'name': 'Holberton school' into the 'school' collection of the given database.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client[db_name]
    result = db.school.insert_one({"name": "Holberton school"})
    print("Document inserted with _id:", result.inserted_id)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-insert.py <database_name>")
        sys.exit(1)
    insert_school_document(sys.argv[1])
