#!/usr/bin/env python3
"""Module that provides some stats about Nginx logs
stored in MongoDB
"""
from pymongo import MongoClient
import pymongo


client = MongoClient('mongodb://127.0.0.1:27017')
ngnix_collection: pymongo.collection.Collection \
    = client.logs.nginx
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print(f"{ngnix_collection.count_documents({})} logs")
print("Methods:")

for method in methods:
    method_count = ngnix_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {method_count}")

status_req_count = ngnix_collection.count_documents({
    "method": "GET",
    "path": "/status"
})

print(f"{status_req_count} status check")

client.close()
