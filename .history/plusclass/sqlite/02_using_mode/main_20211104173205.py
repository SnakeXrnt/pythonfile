
import sqlite3

from employee import Employee

conn = sqlite3.connect('employee.db')

cur = conn.cursor()

emp0 = Employee('Anas','Azhar')