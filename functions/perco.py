def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f

def perco(n,r):
	a=fact(n)
	b=fact(r)
	c=fact(n-r)
	p=a/(c*b)
	co=a/c
	print "nCr is : ",p
	print "nPr is : ",co

n=input("Enter value for n : ")
r=input("Enter value for r : ")
perco(n,r)
	
