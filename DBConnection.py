'''
import pymysql
conn=pymysql.connect(host='*',
                     user="*",
                     password="*",
                     db="*",
                     charset="utf8",
                     cursorclass=pymysql.cursors.DictCursor)
if not conn==None:
    print('connected')
    print(conn.db)
    conn.close()
'''

import sqlite3
try:
    conn=sqlite3.connect('pythonStudy.db')
    cursor=conn.cursor()
    #cursor.execute('create table user(id bigint(10) primary key,name varchar(20))')
    cursor.execute('insert into user(id,name)values(1,"xiaoming")')
    cursor.execute('insert into user(id,name)values(2,"LiLei")')
    cursor.execute('insert into user(id,name)values(3,"tiantian")')
except Exception as result:
    print('异常：',result)
finally:
    if not conn==None:
        print('conn is not close')
    print(conn==None)


cursor.execute('select * from user limit 10')
result1=cursor.fetchall()
print(result1)

cursor.execute('update user set name=? where id=?',('mike',3))
cursor.execute('select * from user where id>?',(2,))
result2=cursor.fetchall()
print(result2)

cursor.execute('delete from user where id=?',(1,))
cursor.execute('select * from user limit 10')
result1=cursor.fetchall()
print(result1)

data=[(4,'daxiong'),(5,'baicai'),(6,'meidi')]
try:
    cursor.executemany('insert into user(id,name) values(?,?)',data)
    conn.commit()
except Exception as ex:
    print('批量insert异常:',ex)
    conn.rollback()

cursor.execute('select * from user limit 10')
result1=cursor.fetchall()
print(result1)