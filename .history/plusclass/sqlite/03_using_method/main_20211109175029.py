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
    
    def get_all_emps(self):
        with self.settings.CONN:
            self.settings.CUR.execute('SELECT * FROM employees ORDER BY first')
        return self.settings.CUR.fetchall()
    

#    def insert_emp(self,emp):
#        self.settings.CUR.excute('INSERT INTO employees VALUES (:first,:last,:salary)',{'first':emp.first,'last':emp.last,'salary':emp.salary})

    def insert_emp(self,emp):
        with self.settings.CONN:
            self.settings.CUR.excute('INSERT INTO employees VALUES (:first,:last,:salary)',{'first':emp.first,'last':emp.last,'salary':emp.salary})

    def mainloop(self):
        
        while True:
            system('cls')
            print(self.settings.MENU)
            option = input('Option : ').lower()
            if option == 'q':
                print('Thanks')
                break
            elif option == '1':
                system('cls')
                users = self.get_all_emps()
                print(users)
                input('Press E')
                
        self.settings.CONN.close()

if __name__ == '__main__':
    app = App()
    app.mainloop()