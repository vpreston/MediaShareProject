import pymongo
import datetime

from pymongo import MongoClient
<<<<<<< HEAD
client = MongoClient('snapcracklepop',27017)
=======
client = MongoClient('mongodb://alex:tester@dharma.mongohq.com:10075/mediashareproject')


db = client.mediashareproject
>>>>>>> 02e9c0c2f73e420a5f99ed8c01338b363ea20c08


posts = db.posts


print posts

for post in posts.find():
    for key in post:
        print key, post[key]
