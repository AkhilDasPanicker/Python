#akhil gokuldas

def fibb(n):
	a=0
	b=1

	i=2
	print a,b,
	while(n>i):
		c=a+b
		a=b
		b=c
		i=i+1
		print c,

print "Enter number of fibonacci series numbers required "
n=input()
fibb(n)


	
