#P = (8, 2, 1, 6, 5, 7, 4, 3, 9)
#P = (0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15)
P = (5,1,4,2,3)

i = 0
found = [[1]]
j = 1
print found
while j < len(P):
	if found[-1][-1] < P[j]:
		found.append( found[-1] + [P[j]] )
	else:
		for i in xrange(len(found)-1,-1,-1):
			if found[i][-1] < P[j]:
				found[i+1] = found[i] + [P[j]]
				break
	print found
	j += 1

