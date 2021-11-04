import sqlite3

connection = sqlite3.connect("empolyee.db")

cursor = connection.cursor() # c / cur 
'''
cursor.execute("""
    CREATE TABLE employees (
    first TEXT,
    last TEXT,
    salary INTEGER
    )     
    """)
'''
#cursor.execute('INSERT INTO employees VALUES ('anisa','azhari',8000000)") "

cursor.execute('SELECT * FROM employees')

emps = cursor.fetchall()
for row 


connection.commit()
connection.close