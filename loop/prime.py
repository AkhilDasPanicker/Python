print "Enter a number "
n=input()

	
k=1

for i in range(2,n):
	if((n%i)==0):
        	k=0
if(n==1):
	print n," is not a prime Number "
elif(k):
	print n," is a prime Number "
else:	
	print n," is not a Prime Number "
