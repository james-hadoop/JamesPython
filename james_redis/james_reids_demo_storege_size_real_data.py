# -*- coding: utf-8 -*-
import redis

client = redis.StrictRedis(host='127.0.0.1', port=6379)
strBasicKey = "key"
strBasicValue = "value"
for i in range(0, 10):
    client.set(strBasicKey + str(i), strBasicValue + str(i))
    client.hset("hashkey", strBasicKey + str(i), strBasicValue + str(i))

print("done!")
