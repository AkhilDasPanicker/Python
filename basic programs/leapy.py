#akhil gokuldas

print "Enter a Year "
year=input()

if(year%400==0):
        print year," is a leap Year "
elif(year%100==0):
        print year," is not a leap Year "
elif(year%4==0):
        print year," is a leap Year "
else:
	print year," is not leap Year "	

