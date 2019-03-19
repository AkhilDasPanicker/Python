def prime(n,x):
      if(x>1):
            if(n%x==0):
		return 1
	    else :
		return prime(n,x-1)
a=input("Enter a Number : ")
b=2
b=prime(a,a-1)

if(b==1):
	print "not prime "
else:
	PRINT "Prime "


