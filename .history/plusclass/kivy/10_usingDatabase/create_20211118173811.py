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
            intrest TEXT DEFAULT "" NOT NULL,
            pic TEXT DEFAULT "default.png" NOT NULL)
        """) #DOC STRING/ comment 
    settings.cur,execute ("""SELECT * FROM user WHERE username = 'admin' """)
    admin = settings.fetchone()
    
    if not admin:
        admin = user(username='admin',first='super',last='admin')
        password = getpass('Input New Password For Admin \nPassword : ')
        retypr_password = getpass('ReType Newly Made Admin Password \nPassword : ')
        
    else:
        print('admin already exists')
    
if __name__ == '__main__':
    main()