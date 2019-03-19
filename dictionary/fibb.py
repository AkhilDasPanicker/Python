def f(n,q,w):
	if n==0:
		return 0
	elif n==1 or n==2:
		return 1
	else:
		for i in range(2,n):
			s=q+w
			q=w
			w=s
		return s
a=input("enter the number")
b={"fib":0}
b["fib"]=f(a,0,1)
print b["fib"]

		
	
