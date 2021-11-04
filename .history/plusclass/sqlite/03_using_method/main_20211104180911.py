from os import system 

from settings import Settings
from employee import Employee

class App:
    def __init__(self):
        self.settings = Settings()
        self.settings.CUR.execute("""
            CREATE TABLE IF NOT EXISTS employees (
            first TEXT,
            last TEXT,
            salary INTEGER
            )                                              
            """)

    def insert_emp(self,emp):
        self.settings.CUR.excute()
    
    def mainloop(self):
        
        while True:
            system('cls')
            print(self.settings.MENU)
            option = input('Option : ').lower()
            if option == 'q':
                print('Thanks')
                break

if __name__ == '__main__':
    app = App()
    app.mainloop()