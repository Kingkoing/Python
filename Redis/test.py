#!/usr/bin/python3
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)  
r.set('foo', 'bar')
x = r.get('foo')
print (str(x))
