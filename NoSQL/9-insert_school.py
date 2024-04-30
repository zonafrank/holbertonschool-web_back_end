#!/usr/bin/env python3
"""Module for function that inserts a new document in a
collection based on kwargs
"""
import pymongo
from typing import Dict, Any
from bson.objectid import ObjectId

def insert_school(
        mongo_collection: pymongo.collection.Collection,
        **kwargs: Dict[Any, Any]) -> ObjectId:
    """inserts a new document in a collection based on kwargs"""
    response = mongo_collection.insert_one(kwargs)
    return response.inserted_id
