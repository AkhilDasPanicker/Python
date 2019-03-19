n=input( "Enter Number of Elements ")
l=[]
for i in range(n):
	e=raw_input("Enter Element ")
	l.append(e)
d=raw_input("Enter element to delete ")
index=l.index(d)
del l[index]
print l 
