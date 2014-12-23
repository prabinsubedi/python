import sys
import gzip
s = sys.argv[1]
count = 0
if s.endswith ('.gz'):
  fg = gzip.open(s,'rb')
  for line in fg:
	count = count +1
  print line,
  print 'Line Count:',count 
  fg.close()
else:
  f = open (s,'r')
  for line in f:
    count = count +1
  print line,
  print 'Line count:',count
  f.close()