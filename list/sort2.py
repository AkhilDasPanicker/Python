a=[]
n=input("enter the elements")
while len(a)<n:
	item=input("enter the item")
	a.append(item)
for i in range(n):
	k=i
	small=a[i]
	for j in range (i+1,n):
		if(a[j]<small):
			small=a[j]
			k=j
	temp=a[i]
	a[i]=small
	a[k]=temp
print a
