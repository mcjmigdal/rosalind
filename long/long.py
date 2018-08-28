from Bio import SeqIO

inp = SeqIO.parse("long.txt", 'fasta')
inp = [ fa.seq for fa in inp ]

def match(A,B):
	i = 0
	j = 0
	while i <= len(A):
		if A[-1-i:] == B[:1+i]:
			j = i
		i += 1
	return j

def perm(A,L):
	p = [ (A,l) for l in L ]
	p += [ (l,A) for l in L ]
	return p

while len(inp) > 1:
	C = [ c for c in perm(inp[0],inp[1:]) ]
	m_prev = (0,0)
	for c in C:
		m = match(c[0],c[1])
		if m > m_prev[0]:
			m_prev = (m, c)
	A, B = m_prev[1]
	inp.append(A[:-1-m_prev[0]] + B)
	inp = [ i for i in inp if not i == m_prev[1][0] and not i == m_prev[1][1] ]
	print len(inp)

print inp[0]	
