n=input( "Enter Number of Elements ")
l=[]
for i in range(n):
	e=raw_input("Enter Element ")
	l.append(e)
a=l
a.sort()
s=a[1]
v=l.index(s)

print "Second Largest Element is : ",s
print "Position : ",v
