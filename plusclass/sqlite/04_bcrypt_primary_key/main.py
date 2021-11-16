from os import system
import bcrypt

from settings import Settings
from employee import Employee

class App:
	
	def __init__(self):
		self.settings = Settings()
		self.get_last_id()

	def get_last_id(self):
		self.settings.CUR.execute("SELECT * FROM employees ORDER BY id DESC LIMIT 1")
		emp = self.settings.CUR.fetchone()
		Employee.counter = emp[0]+1

	def get_all_emps(self):
		with self.settings.CONN:
			self.settings.CUR.execute("SELECT * FROM employees ORDER BY first")
		return self.settings.CUR.fetchall()

	def insert_emp(self, emp):
		with self.settings.CONN:
			self.settings.CUR.execute("INSERT INTO employees VALUES (:id, :username, :password, :first, :last, :salary)", {"id":emp.id, "username":emp.username, "password":emp.password, "first":emp.first, "last":emp.last, "salary":emp.salary})

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
				username, first, last, salary = input().split()
				emp = Employee(username, first, last, salary)

				password = input("Enter New Password:")
				repassword = input("Enter New Password:")

				while password != repassword:
					print("Password doesn't match")
					repassword = input("ReEnter New Password: ")
				else:
					emp.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

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