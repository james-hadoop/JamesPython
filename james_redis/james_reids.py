#-*- coding: utf-8 -*-
import redis

client = redis.StrictRedis(host='127.0.0.1', port=6379)
key = "hello"
setResult = client.set(key, "python-redis")
print(setResult)
value = client.get(key)
print(f"{key} -> {value}")

# 1.string
# 输出结果: True
client.set("hello", "world")
# 输出结果: world
client.get("hello")
# 输出结果: 1
client.incr("counter")
# 2.hash
client.hset("myhash", "f1", "v1")
client.hset("myhash", "f2", "v2")
# 输出结果: {'f1': 'v1', 'f2': 'v2'}
ret = client.hgetall("myhash")
print(ret)
# 3.list
client.rpush("mylist", "1")
client.rpush("mylist", "2")
client.rpush("mylist", "3")
# 输出结果: ['1', '2', '3']
client.lrange("mylist", 0, -1)
# 4.set
client.sadd("myset", "a")
client.sadd("myset", "b")
client.sadd("myset", "a")
# 输出结果: set(['a', 'b'])
client.smembers("myset")
# # 5.zset
# client.zadd("myzset", "99", "tom")
# client.zadd("myzset", "66", "peter")
# client.zadd("myzset", "33", "james")
# # 输出结果: [('james', 33.0), ('peter', 66.0), ('tom', 99.0)]
# client.zrange("myzset", 0, -1, withscores=True)
#
# pipeline = client.pipeline(transaction=False)
# pipeline.set("hello", "world")
# pipeline.incr("counter")
# # [True, 3]
# result = pipeline.execute()
