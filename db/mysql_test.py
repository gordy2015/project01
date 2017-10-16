
import pymysql

conn = pymysql.connect(host='192.168.2.11',port=3306,user='ruigao',passwd='ruigao2016',db='pydb')

a = 'af'
b = 'a'
cur = conn.cursor()
# s = cur.execute("create table news(title VARCHAR(30), content VARCHAR(100))")
# print(s)
s = cur.execute("insert into user values( %s, %s)",(a,b) )
print(s)
if s:
    print('insert success')
else:
    print('insert false')
# q = cur.fetchall()
# print(q)

# print(type(q))
# USR = []
# for i,k,t in q:
#    # print(i,k,t)
#     dict = {"ip":i,"hostname":k,"version":t}
#     print(dict)
#     USR.append(dict)
# print(USR)




# if s:
#     print('success')
# else:
#     print('false')
# # print(len(w))
# # for i in w:
# #     print(i)
conn.commit()   #insert语句要记得commit
conn.close()