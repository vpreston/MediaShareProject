import pymongo
import datetime

from pymongo import MongoClient
<<<<<<< HEAD
client = MongoClient('mongodb://sofdes:sofdes@dharma.mongohq.com:10075/mediashareproject')
=======
>>>>>>> 4d9eb172c15e401ab0f75dde2787521eb3b6ef8b

client = MongoClient('mongodb://alex:test@dharma.mongohq.com:10075/mediashareproject')

<<<<<<< HEAD
=======

db = client.mediashareproject
>>>>>>> 4d9eb172c15e401ab0f75dde2787521eb3b6ef8b
posts = db.posts

print posts

for post in posts.find():
    for key in post:
        print key, post[key]
