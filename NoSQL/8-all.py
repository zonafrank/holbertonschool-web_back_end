#!/usr/bin/env python3
"""Module that lists all documents in a collection"""
import pymongo
from typing import List, Any

import pymongo.collection


def list_all(
        mongo_collection: pymongo.collection.Collection
        ) -> List[Any]:
    """lists all documents in a collection"""
    return [doc for doc in mongo_collection.find()]
