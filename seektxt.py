f=open('sample.txt','r')
f.seek(10)
print('position after seek is',f.tell())
f.close()

