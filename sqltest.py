import pymysql

con = pymysql.connect(
    host='192.168.109.5', 
    user='yglee', 
    password='1234',
    database='madang',
    port=4567,
    charset='utf8',
    autocommit=True
)

cursor = con.cursor()
sql="SELECT * FROM Book;"
cursor.execute(sql)
con.cursor().execute(
    "insert into Book (bookid,bookname,publisher,price) values('19','데베시 연습2','연코딩','500')")
rows = cursor.fetchall()
con.close()
print(rows)