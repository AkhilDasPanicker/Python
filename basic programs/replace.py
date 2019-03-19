n=input( "Enter Number of Elements ")
l=[]
for i in range(n):
	e=raw_input("Enter Element ")
	l.append(e)
print l

a=raw_input("Enter the element to be Replaced ")
i=l.index(a)
g=raw_input("Enter the element to be inserted ")
l[i]=g
print "List after Replacement "
print l


