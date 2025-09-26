class College:
	def clg(self):
		print("vit-b college")
class Dept:
	def cse(self):
		print("cse department")
class Student(College,Dept):
	def std(self):
		print("vit-b cse student")
s=Student()
s.clg()
s.cse()
s.std()			
