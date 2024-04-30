#!/usr/bin/env python3
"""Module for update_topics function"""
import pymongo
import pymongo.collection
from typing import List


def update_topics(
        mongo_collection: pymongo.collection.Collection, 
        name: str, topics: List[str]) -> None:
    """changes all topics of a school document based on the name"""
    mongo_collection.update_many(
        {"name": name}, 
        {"$set": {"topics": topics}})
