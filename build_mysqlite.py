# coding=utf-8
import sqlite3

conn = sqlite3.connect('d:/info.db')
curs = conn.cursor()
curs.execute("PRAGMA foreign_keys = ON")

def create_tables():
    with open('build_tables.sql', encoding='utf-8', mode='r') as f:
        sql_list = f.read().split(';')[:-1]
        for x in sql_list:
            curs.execute(x)
    conn.commit()
    print("table created.")

def insert_data():
    with open('insert_data.sql', encoding='utf-8', mode='r') as f:
        sql_list = f.read().split(';')[:-1]
        for x in sql_list:
            curs.execute(x)
    conn.commit()
    print("date has inserted.")

# create_tables()
# insert_data()
# result = curs.execute('select * from sqlite_master where type = "table"')
# for i in result:
#     print(i)

sql = 'select * from stu_course'
curs.execute(sql)
list = curs.fetchall()
for rec in list:
    print(rec)
