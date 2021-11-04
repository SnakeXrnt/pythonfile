
import sqlite3

from employee import Employee

conn = sqlite3.connect('employee.db')

cur = conn.