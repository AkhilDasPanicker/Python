a=[]
p=0
n=input("enter the number of elements")
while len(a)<n:
	item=input("enter the item")
	a.append(item)

x=input("enter the element to search")
for i in range(0,n):
	if(a[i]==x):
		print "found",a[i]
		p=1

if(p==0):
	print "not found"

