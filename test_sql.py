import config
import telebot
from telebot import apihelper
import urllib.request 
import pyodbc
from datetime import datetime

driver = 'DRIVER={SQL Server}'
server = 'SERVER=dc-sql12-db\\db'
db = 'DATABASE=Inventory'
conn_str = ';'.join([driver, server, db])
 
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
 
cursor.execute("SELECT * FROM dbo.main WHERE hostname = '90514-ws404' ")
row = cursor.fetchone()
rest_of_rows = cursor.fetchall()
for item in rest_of_rows:
   print(item)