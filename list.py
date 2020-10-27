classmate=['moke','john','jet','mike']
print("classmate len:",len(classmate))
print(classmate[-2])   #-1最后元素索引,-2倒数第二
classmate.append('jonh')
classmate.insert(2,"hady")
print(classmate[-1])
print(classmate[1:3]) #切片
print(classmate[:3]) #切片 0可以省略
classmate.insert(-1,'john')
print(classmate)
classmate.pop()

print(classmate)
classmate.pop(0)
print(classmate)
classmate.remove("mike")
for ele in enumerate(classmate):
    print('ele:',ele)
del classmate

untitle=['Python',28,"人生苦短，我用Python",["爬虫","自动化运维","云计算"]]
for ele in untitle:
    print(ele)
