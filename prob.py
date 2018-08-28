from sys import argv
import math
with open(argv[1]) as inp:
	s = inp.readline().strip()
	P = inp.readline().strip().split()
	P = [ float(x) for x in P ]
PS = []
for p in P:
	d = { 'G' : p/2, 'C' : p/2, 'A' : (1-p)/2, 'T' : (1-p)/2 }
	ps = 1
	for l in s:
		ps *= d[l]
	PS.append(math.log10(ps))
print ' '.join([str(x) for x in PS])
