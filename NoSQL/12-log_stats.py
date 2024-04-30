#!/usr/bin/env python3
"""This module provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    total_count = collection.count_documents({})
    print('{} logs'.format(total_count))

    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method" : method})
        print('\tmethod {}: {}'.format(method, method_count))

    status_count = collection.count_documents({'path': "/status"})
    print('{} status check'.format(status_count))