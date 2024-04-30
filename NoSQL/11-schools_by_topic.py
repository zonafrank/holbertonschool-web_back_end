#!/usr/bin/env python3
"""Module for function school_by_topic"""
import pymongo
from typing import List, Dict, Any


def schools_by_topic(
        mongo_collection: pymongo.collection.Collection, 
        topic: str) -> List[Dict[Any, Any]]:
    """returns the list of school having a specific topic"""
    return [school for school 
            in mongo_collection.find({"topics": {"$in": [topic]}})]
