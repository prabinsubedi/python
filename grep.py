import sys
import gzip
s = sys.argv[1]
s2 = sys.argv[2]

if s2.endswith('.gz'):
	fg = gzip.open(s2,'rb')
	for line in fg:
		if s in line:
			print s

	fg.close()
else:
	f = open (s2,'rb')
	for line in f:
		if s in line:
			print s 
	f.close()		

