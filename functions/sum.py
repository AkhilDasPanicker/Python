def sum(n):
	if(n==0):
		return 0
	else:
		return (n%10)+sum(n/10)
	

n=input("Enter a Number : ")
su=sum(n)

print "Sum of digits of ",n,"  is ",su

		
