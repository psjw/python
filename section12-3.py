# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제
import sqlite3

# DB 생성(파일)
conn=sqlite3.connect('C:/ljw-study/python/PYTHON_BASIC/resource/database.db')#본인 DB 경로

#Cursor 연결
c=conn.cursor()

#데이터 수정1
# c.execute("UPDATE users SET username=? where id =? ",('niceman',2))



# 데이터 수정2
# c.execute("UPDATE users SET username=:name where id =:id ",{'name':'goodman','id':5})


# 데이터 수정3
# c.execute("UPDATE users SET username='%s' where id ='%s' " % ('badboy',3))




# 중간데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)


# Row Delete1
c.execute("DELETE FROM users where id=?",(2,))

# Row Delete2
c.execute("DELETE FROM users where id=:id",{"id":4})

# Row Delete4
c.execute("DELETE FROM users where id='%s'"%(5))


print('-----------')
# 중간데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)

# 테이블 전체 데이터 삭제
print('users db deleted : ',conn.execute("DELETE FROM users").rowcount," rows")

# 커밋
conn.commit()

# 접속 해제
conn.close()