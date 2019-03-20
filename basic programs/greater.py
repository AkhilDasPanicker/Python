#akhil gokuldas

print "Enter First Number "
a=input()
print "Enter Second Number "
b=input()
print "Enter Third Number "
c=input()

if((a==b)and(a==c)):
	print "The given numbers are equal "
elif((a>b)and(a>c)):
	print a," is greater "
elif((b>a)and(b>c)):
	print b," is greater "
else:
	print c," is greater "
