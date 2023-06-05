import mysql.connector

from scraper import scrapers
datalist=scrapers()
mydb = mysql.connector.connect(
host="localhost",
user="root",
password=""
)
cur=mydb.cursor()
cur.execute("DROP DATABASE Bseindia")
cur.execute("CREATE DATABASE IF NOT EXISTS Bseindia")
cur.execute("USE Bseindia")
cur.execute('''CREATE TABLE IF NOT EXISTS `bseindia`(
    Deal_date varchar(100) not null,
    security_code int not null,
    Securite_name varchar(100) not null,
    Client_Name	 varchar(100) not null,
    Deal_Type varchar(100) not null,
    Quantity	int not null,
    Price FLOAT not null)''')
for i in datalist:
    cur.execute('''INSERT INTO bseindia (Deal_date,security_code,Securite_name,Client_Name,Deal_Type,Quantity,Price)
    VALUES (%s,%s,%s,%s,%s,%s,%s)''',(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    mydb.commit()
cur.close()
mydb.close()
