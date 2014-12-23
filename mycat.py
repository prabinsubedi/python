import sys
import gzip

s = sys.argv[1]

if s.endswith ('.gz'):
  fg = gzip.open(s,'rb')
  for line in fg:
	print line,
  fg.close()
else:
  f = open (s,'r')
  for line in f:
    print line,
  f.close()

