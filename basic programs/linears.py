#akhil gokuldas

n=input("Enter Number of Elements ")
l=[]
for i in range(n):
	u=raw_input("Enter element ")
        l.append(u)
v=raw_input("Enter element to be searched ")
k=0
for i in range(n):
	if v==l[i]:
		k=1
if(k==1):
	print "Element Found..."
else:
	print "Not found "
	
