import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    port='3306',
    password="root",
    database="hello"
)
print("connection established")
mycursor=mydb.cursor()
mycursor.execute("create table student(id int,name varchar(50),address varchar(50))")
print("Table created")

q="insert into student values (1,'Anu','Anu Bhavan')"
mycursor.execute(q)
mydb.commit()

sql="insert into student values(%s,%s,%s)"
val=[(2,'Nisha','Nisha Bhavan'),
     (3,'Minu','Minu Navas')]
mycursor.executemany(sql,val)
mydb.commit()

mycursor.execute("select * from student")
print(mycursor)
res=mycursor.fetchall()
print(res)

for i in res:
    print(i)
print()

mycursor.execute("select * from student where id=2")
print(mycursor)
oneres=mycursor.fetchone()
print(oneres)

for i in oneres:
    print(i)





