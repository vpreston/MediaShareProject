#!/usr/bin/python

"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html


Setup:

1) Go to redistogo.com and create a free Nano database.

   Note the host, port and authcode.  

   Add the host and port info to the Model object
   below.  In general you don't want to put authcodes in your
   programs (unless you want to make the database globally accessible).

   Instead, add a line like this to your .bashrc file:

export REDIS_AUTH="374238957839837549872349577"

   To re-run the .bashrc file, run this at the linux prompt

$ . ~/.bashrc

2) Install the python-redis package

sudo apt-get install python-redis

3) Run this program

python redis_demo.py
"""

import os
import random
import redis
import sys




def main():
    host = 'koi.redistogo.com'
    port = 10241

    try:
        password = 'dfe292746a6f00cb217d943afd8dc555'
    except KeyError:
        print 'Environment variable REDIS_AUTH is not set.'
        sys.exit()
        
    rdb = redis.Redis(host=host, port=port,password=password,db=0)
    print rdb

    # http://redis.io/commands#string
    # 'foo' is the name of the set, bar is the data
    rdb.set('foo', 'bar')
    rdb.append('foo', 'bar')
    print rdb.get('foo')

    # http://redis.io/commands#hash
    for c in 'abcdefg':
        score = random.random()
        rdb.hset('word_freq',c, score)
        rdb.rpush('scorelist', {c:rdb.hget('word_freq', c)})
    print rdb.lrange('scorelist', 0, 6)
    # http://redis.io/commands#list
    rdb.rpush('list', 'elt1')
    rdb.rpush('list', 'elt2')
    print rdb.lindex('list', 0)

    # http://redis.io/commands#set
    for c in 'allen':
        rdb.sadd('set', c)
    rdb.sunion('set', set('downey'))
    print rdb.smembers('set')


if __name__ == '__main__':
    main()

