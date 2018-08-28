P = [ 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 ]
#P = (8, 2, 1, 6, 5, 7, 4, 3, 9)

print P
mstart = 0
L = [mstart]
j = 1
while j < len(P):
	if P[L[-1]] < P[j]:
		L.append(j)
	else:
		for i in xrange(len(L)-2,-1,-1):
			if P[L[i]] < P[j]:
				L[i+1] = j
				break
	j += 1
	print [ P[k] for k in L ]
