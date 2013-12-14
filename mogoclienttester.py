import pymongo
import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://sofdes:sofdes@dharma.mongohq.com:10075/mediashareproject')

db = client.mediashareproject

posts = db.posts

print posts

for post in posts.find():
    for key in post:
        print key, post[key]
