#import requests
#import bs4
import sqlite3 as s
conn=s.connect('results.db')
c=conn.cursor()
#c.execute('''
# CREATE TABLE Departments (sno integer primary key autoincrement,
# dep_code text unique,
# dep_name text)
# '''
#)
for i in range(111720000001,111721000001,1000):
    print(i)

conn.commit()
conn.close