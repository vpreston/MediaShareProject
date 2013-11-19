import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient()


db = client.test_database
posts = db.posts
print posts

for post in posts.find():
    for key in post:
        print key, post[key]
