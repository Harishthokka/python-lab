class College:
	def clg(self):
		print("vit-b college")
class Dept(College):
	def cse(self):
		print("cse department")
class Student(Dept):
	def std(self):
		print("vit-b cse student")
s=Student()
s.clg()
s.cse()
s.std()	
