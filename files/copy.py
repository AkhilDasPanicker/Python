def copy(f1,f2):
	opener1=open(f1,"r")
	opener2=open(f2,"w")
	reader=opener1.read()
	opener2.write(reader)
	opener1.close()
	opener2.close()
copy("txt","abc")
print "contents has been copied"
