print "Enter number of fibonacci series numbers required "
n=input()

a=0
b=1

i=2
print a
print b

while(n>i):
	c=a+b
        a=b
        b=c
        i=i+1
        print c
