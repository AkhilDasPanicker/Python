def small(x,y):
	big=a
	small=b
	if(b>a):
		big=b
		small=a
	return big,small
a=input("enter first no")
b=input ("enter second no")
a,b=small(a,b)
print "a is",a
print "b is",b
