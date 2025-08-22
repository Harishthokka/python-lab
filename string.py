a="string"
print(a)
print("//reverse")
print(a[::-1])
print("//reverse without slice ")
rev=""
for i in a:
	rev=i+rev
print(rev)
print("//palindrom")
if a==a[::-1]:
	print(a,"is palindrom")
else:
	print(a,"is not a palindrom")
print("//length without method")
c=0
for i in a:
	c+=1
print("length is",c)
print("//vowels in string")
vowels="aeiou"
c=0
for i in a:
	if i in vowels:
		c+=1
print("no.of vowels",c)
print("//even length words in string")
s="you are enough"
w=s.split()
for i in w:
	if len(w)%2==0:
		print(i)
		 
