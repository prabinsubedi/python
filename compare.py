import sys
import gzip
import difflib 
from difflib import Differ 

s = sys.argv[1]
s2 = sys.argv[2]


if s.endswith('.gz') and s2.endswith('.gz'):
	with gzip.open(s,'rb') as f, gzip.open (s2,'rb') as fg:
		flines = f.readlines()
		glines = fg.readlines ()
		d = difflib.Differ()
		diff = d.compare(flines, glines)
		print ''.join(diff)
	
elif s2.endswith('.gz'): 
	with gzip.open(s2,'rb') as fg, open (s,'rb') as f:
		glines = fg.readlines()
		flines = f.readlines()
		d = difflib.Differ()
		diff = d.compare(glines, flines)
		print ''.join(diff)

elif s.endswith ('.gz'):
	with gzip.open(s,'rb') as fg, open (s2,'rb') as f:
		glines = fg.readlines()
		flines = f.readlines()
		d = difflib.Differ()
		diff = d.compare(glines, flines)
		print ''.join(diff)

else:
	with open(s,'rb') as fg, open (s2,'rb') as f:
		glines = fg.readlines()
		flines = f.readlines()
		d = difflib.Differ()
		diff = d.compare(glines, flines)
		print ''.join(diff)
f.close()
fg.close()
