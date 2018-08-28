def all_perms(elements):
	if len(elements) <= 1:
		yield elements
	else:
		for perm in all_perms(elements[1:]):
			for i in range(len(elements)):
				yield perm[:i] + elements[0:1] + perm[i:] 

print len([ i for i in all_perms([1,2,3,4,5,6])])
for i in all_perms([1,2,3,4,5,6]):
	print ' '.join([str(z) for z in i])
