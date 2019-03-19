def facto(n):
	if(n==0 or n==1):
		return 1
	else:
		return n*facto(n-1)

print "Enter a number "
n=input()
print(facto(n))

