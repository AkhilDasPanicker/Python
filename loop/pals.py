s=raw_input("Enter a string ")

n=len(s)
r=n-1
temp=s[r]
r=r-1
for i in range(1,n):
	temp=temp+s[r]
	r=r-1


if(temp==s):
	print "Palindrome "
else:
	print "Not Palindrome "










