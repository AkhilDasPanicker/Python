

e=raw_input("Enter Element ")
f=e.split()

b=e[::-1]
print "Reverse Order "
print b
print "Alphabetical Order "
f.sort()
for i in range(len(f)):
	print f[i]," ",
