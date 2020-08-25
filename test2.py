import pyodbc # для взаимодействия с БД
import pandas as pd # для манипулирования данными и экспорта в виде электронных таблиц


driver = 'DRIVER={SQL Server}'
server = 'SERVER=dc-sql12-db\\db' # имя сервера
db = 'DATABASE=Inventory' # имя БД
conn_str = ';'.join([driver, server, db]) 
conn = pyodbc.connect(conn_str) # Подключение БД

script = """
SELECT * FROM dbo.main WHERE hostname = '90514-ws404'
""" # скрипт запроса к БД

df = pd.read_sql_query(script, conn) # чтение полученых данных с занесением в переменную

writer = pd.ExcelWriter('documents\\example.xlsx') # создание файла
df.to_excel(writer, sheet_name='bar') # Добавление данных из переменной с созданием листа
writer.save() # сохранение