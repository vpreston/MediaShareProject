import pymongo
import datetime

from pymongo import MongoClient
client = MongoClient('snapcracklepop',27017)


db = client.test_database
posts = db.posts
print posts

for post in posts.find():
    for key in post:
        print key, post[key]
