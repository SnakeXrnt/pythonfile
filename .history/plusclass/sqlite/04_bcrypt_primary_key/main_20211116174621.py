from os import system

from settings import Settings
from employee import Employee

class App:
	
	def __init__(self):
		self.settings = Settings()

	def get_all_emps(self):
		with self.settings.CONN:
			self.settings.CUR.execute("SELECT * FROM employees ORDER BY first")
		return self.settings.CUR.fetchall()

	def insert_emp(self, emp):
		with self.settings.CONN:
			self.settings.CUR.execute("INSERT INTO employees VALUES (:first, :last, :salary)", {"first":emp.first, "last":emp.last, "salary":emp.salary})

	def find_emp(self, first):
		with self.settings.CONN:
			self.settings.CUR.execute("SELECT * FROM employees WHERE first=:first", {"first":first}) #primary key (unik)
		return self.settings.CUR.fetchone()

	def update_salary(self, emp, new_salary):
		with self.settings.CONN:
			self.settings.CUR.execute("UPDATE employees SET salary=:salary WHERE first=:first", {"salary": new_salary, "first":emp.first})

	def remove_employee(self, emp):
		with self.settings.CONN:
			self.settings.CUR.execute("DELETE FROM employees WHERE first=:first AND last=:last", {"first":emp.first, "last":emp.last})

	def mainloop(self):
		
		while True:
			system("cls")

			print(self.settings.MENU)

			option = input("Option : ").lower()
			if option == "q":
				print("Thanks")
				break
			elif option == '1':
				system("cls")
				emps = self.get_all_emps()
				print(emps)
				input("Press Enter to Return")
			elif option == '2':
				system("cls")
				first, last, salary = input().split()
				emp = Employee(first, last, salary)

				password = input('Enter new Password : ')
				
				self.insert_emp(emp)
				print("DONE!!")
				input("Press Enter to Return")
			elif option == '3':
				system("cls")
				first = input()
				res = self.find_emp(first)
				if res:
					print(res)
				else:
					print("There's no such name here")
				input("Press Enter to Return")
			elif option == '4':
				system('cls')
				first, last, salary, new_salary = input().split()
				res = self.find_emp(first)
				if res:
					emp = Employee(first, last, salary)
					res2 = self.update_salary(emp, new_salary)
				else:
					print("There's no such name here")
				input("Press Enter to Return")
			elif option == '5':
				system('cls')
				first, last, salary = input().split()
				res = self.find_emp(first)
				if res:
					emp = Employee(first, last, salary)
					yesno = input("Are you sure to remove this user ?(y/n)")
					if yesno.lower() == 'y':
						self.remove_employee(emp)
					else:
						print("Cancelling removing prrocess")
				else:
					print("There's no such name here")

		self.settings.CONN.close()

if __name__ == "__main__":
	app = App()
	app.mainloop()