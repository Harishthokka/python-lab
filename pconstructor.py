class Student:
	def __init__(self,name,pin,branch):
		self.name=name
		self.pin=pin
		self.branch=branch
	def display(self):	
		print("name:",self.name)
		print("pin:",self.pin)
		print("branch:",self.branch)
s1=Student("harish",101,"cse")
s2=Student("nani",102,"ece")
s1.display()
print()
s2.display()
