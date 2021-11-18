import bycrypt 
from getpass import getpass 

from settings import Settings
from models.user import User

def main():
    
    settings = Settings()
    settings.cur.execute("""
                         CREATE 
                         """)