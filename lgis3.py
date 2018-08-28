#P = [ 0, 8, 4 , 12 , 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 ]
#P = (8, 2, 1, 6, 5, 7, 4, 3, 9)
#P = ( 5, 1, 4, 2, 3 )
from sys import argv
inp = argv[1]
P = open(inp).readlines()[1]
P = [ int(p) for p in P.strip().split() ]

mstart = 0
L = [ [P[mstart]] ]
j = 1
while j < len(P):
	if L[-1][-1] < P[j]:
		L.append( L[-1] + [P[j]] )
	elif L[0][0] > P[j]:
		L[0][0] = P[j]
	else:
		for i in xrange(len(L)-2,-1,-1):
			if L[i][-1] < P[j]:
				L[i+1] = L[i] + [P[j]]
				break
	j += 1

print ' '.join( str(l) for l in L[-1])


mstart = 0
L = [ [P[mstart]] ]
j = 1
while j < len(P):
	if L[-1][-1] > P[j]:
		L.append( L[-1] + [P[j]] )
	elif L[0][0] < P[j]:
		L[0][0] = P[j]
	else:
		for i in xrange(len(L)-2,-1,-1):
			if L[i][-1] > P[j]:
				L[i+1] = L[i] + [P[j]]
				break
	j += 1

print ' '.join( str(l) for l in L[-1])
