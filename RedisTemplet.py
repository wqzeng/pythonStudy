# @author :xpzhuang
# @date : 2021/1/1
import redis

r=redis.StrictRedis('47.115.16.193',6379,0)
r.set('name','zengwq')
age=r.incr("age")
name=r.get('name')
print(name)
print(age)

#事务使用
piple=r.pipeline(transaction=True)
piple.set("name","zengwq")
piple.set("age",23)
result=piple.execute()
print(result)