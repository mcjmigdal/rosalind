A, B = open('conv.txt').readlines()
A = [ float(a) for a in A.split() ]
B = [ float(b) for b in B.split() ]

m_prev = 0
for i in range(len(B)):
	for j in range(len(A)):
		d = A[j] - B[i]
		Ad = [ round(a-d) for a in A ]
		Bb = [ round(b) for b in B ]
		m =  len([ a for a in Ad if a in Bb ])
		if m > m_prev:
			m_prev = m
			d_prev = d

print m_prev
print d_prev
