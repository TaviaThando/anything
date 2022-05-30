class Person:
	def __init__(self, gender):
		self.gender = gender

	def greet(self):
		print('Hello')


class User(Person):
	def __init__(self, gender, email, username):
		super().__init__(gender)
		self.email = email
		self.username = username

	def greet(self):
		print(f'{self.username} says hello.')


jake = User('male', 'jake@email.io', 'jake123')
