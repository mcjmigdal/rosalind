from sys import argv
with open(argv[1]) as inp:
	name = inp.readline()
	s = ''
	line = inp.readline().strip()
	s += line
	while line:
		line = inp.readline().strip()
		s += line
	
def FailureArray(s):
	ff = []
	for k in xrange(0,len(s)+1):
		for j in xrange(1,len(s)+1):
			if j > k:
				ff.append(0)
				break
			elif s[j:k+1] == s[:k-j+1]:
				ff.append(k-j+1)
				break
	return ff

def failTable(pattern):
	result = [None]
	for i in range(0,len(pattern)):
		j = i
		
		while True:
			if j == 0:
				result.append(0)
				break
			if pattern[result[j]] == pattern[i]:
				result.append(result[j] + 1)
				break
			j = result[j]
	return result[1:]
print ' '.join([str(x) for x in failTable(s)])
