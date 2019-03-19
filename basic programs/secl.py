a=[]
n=input("Enter number of elements ")
for i in range(n):
	v=input("Enter element ")
	a.append(v)
b=a
b.sort()
c=b[1]
d=a.index(c)
print "Second Smallest Element is ",c
print "Position ",d
