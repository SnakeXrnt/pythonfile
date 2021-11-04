
import sqlite3

class Settings:
    
    CONN = sqlite3.connect('employee.db')
    CUr = CONN.cursor()
    
    MENU = """
(1) SHOW ALL EMPLOYEES 
(2) ADD NEW EM   
"""