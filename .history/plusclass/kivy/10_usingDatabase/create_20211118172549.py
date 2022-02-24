import bycrypt 
from getpass import getpass 

from settings import Settings
from models.user import User

def main():
    
    settings = Settings() #cibstraub
    settings.cur.execute("""
        CREATE TABLE IF NOT EXISTS username (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEST NOT NULL UNIQUE,
            )
        """) #DOC STRING