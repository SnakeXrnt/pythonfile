
import sqlite3

from employee import Employee

conn = sqlite3.connect('employee.db')

cur = conn.cursor()

emp0 = Employee('Anas','Azhar',300000)
emp1 = Employee('Anas1','Azhar1',300000)
emp2 = Employee('Anas','Azhar',300000)