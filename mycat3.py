import sys
import gzip
s = sys.argv[1]
s2 = sys.argv[2]

if s.endswith('.gz') and s2.endswith('.gz'):
	fg = gzip.open(s,'rb')
	file_content = fg.read()
	f = gzip.open(s2,'wb')
	f.write(file_content)

elif s2.endswith('.gz'): 
	f = open (s,'rb')
	file_content = f.read()
	fg = gzip.open(s2,'wb')
	fg.write(file_content)

elif s.endswith ('.gz'):
	fg = gzip.open(s,'rb')
	file_content = fg.read()
	f = open (s2,'wb')
	f.write(file_content)

else:
	f = open (s,'r')
	file_content=f.read()
	fg = open(s2,'wb')
	fg.write(file_content)
f.close()
fg.close()














#for line in file_content:
#	print line,
  
      
	
    


