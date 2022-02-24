import bycrypt 
from getpass import getpass 

from settings import Settings
from models.user import User

def main():
    
    settings = Settings() #cibstraint NOT NULL , UNIQUE
    settings.cur.execute("""
        CREATE TABLE IF NOT EXISTS username (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEST NOT NULL UNIQUE,
            first TEXT NOT NULL,
            last TEXT NOT NULL,
            bio TEXT DEFAULT "" NOT NULL,
            intrest TEXT DEFAULT "" NOT NULL 
            )
        """) #DOC STRING/ comment 
    
if __name__ == '__main__':
    main()