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
#cursor.execute('INSERT INTO employees VALUES ('anisa','azhari',)


connection.commit()
connection.close