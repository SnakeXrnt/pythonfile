
import sqlite3

class Settings:
    
    CONN = sqlite3.connect('employee.db')
    CUr = CONN.cursor()
    
    MENU = """
(1)     
"""