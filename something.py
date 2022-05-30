class Person:
	def __init__(self, gender):
		self.gender = gender

	def greet(self):
		print("hello")


class User(Person):
	def __init__(self, gender, email, username):
		super().__init__(gender)
		self.email = email
		self.username = username

	def greet(self):
		print(f'{self.username} says hello.')


print("I am doing something\n")
def doing_something():
	someone = input("Do you want me to do something? ")

	if someone == "yes":
		print("Thats a shame, I'm lazy")
	else:
		print("That's what I wanted to hear!")


doing_something()


jake = User('male', 'jake@email.io', 'jake123')
