class Student:
	def __init__(self,name):
		self.name=name
		print("constructor call name:",self.name)
	def __del__(self):	
		print("destructor called:",{self.name})
s1=Student("harish")
del s1
