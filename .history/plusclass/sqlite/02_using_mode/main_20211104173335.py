
import sqlite3

from employee import Employee

conn = sqlite3.connect('employee.db')

cur = conn.cursor()

emp0 = Employee('Anas','Azhar',300000)
emp1 = Employee('Anas1','Azhar1',300000)
emp2 = Employee('Anas2','Azhar2',300000)

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
    first TEXT
    )
    """)