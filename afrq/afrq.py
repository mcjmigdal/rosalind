d = open('afrq.txt').read().split()
d = [ float(n) for n in d ]
o = []
for n in d:
	o.append( -n + 2 * n ** 0.5 )

print " ".join([str(round(n,3)) for n in o])	
