#有序列表:元组 tuple,tuple一旦初始化就不能修改
classmates=('moke.tsang','lily','john')
#可以省略括号
classmates_2='moke.tsang','lily','john'
print(classmates_2)
t = ('a', 'b', ['A', 'B'])
t[2][0]='X'
print(t)

#只有1个元素时，不能省略最后的逗号
d = (3,)
print(d)
a=()

verse1=("世界冠军")
verse2=("世界冠军",)
print(type(verse1))
print(type(verse2))
