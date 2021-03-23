import redis
import random
import json
heads = ["snake", "bull", "raven", "bunny"]
rd = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
for _ in range(10):
    randNum = random.randint(0,99)
    head = random.choice(heads)
    rd.set(randNum, head)

for _ in range(10):
    num = random.randint(0,99)
    print(rd.get(num))
