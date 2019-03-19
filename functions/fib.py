def fib(n):
	if(n==0):
		return 0
	elif (n==1):
		return 1
	else:
		return fib(n-1)+fib(n-2)

a=input("Enter Number of Fibonacci Numbers Required ")

for i in range(a):
	print fib(i)
