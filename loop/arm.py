print "Enter a number "
am=input()
s=0
n=am

while(n>0):
	r=n%10
        n=n/10
        s=s+(r*r*r)
if(am==s):
	print am," is an Armstrong Number "
else:
	print am," is not an Armstrong Number " 

