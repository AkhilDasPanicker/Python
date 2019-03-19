str1=raw_input("Enter a String ")

k=1
l=len(str1)

for i in range(l/2):
	if(str1[i]!=str1[l-i-1]):
		k=0
 		break
if(k==1):
	print "Palindrome"
if(k==0):
	print "Not Palindrome "
