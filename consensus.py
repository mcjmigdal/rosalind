def fasta(plik):
	with open(plik) as inp:
		inp = inp.readlines()
		s = []
		a = ''
		for line in inp[1:]:
			if line.startswith('>'):
				s.append(a)
				a = ''
			else:
				a += line.strip() 
	
		s.append(a)
		return s

from sys import argv
fast = fasta(argv[1])
seq_len = len(fast[0])
c = ''
P = {}
for x in 'ATCG':
	P[x] = [0] * seq_len  
for seq in fast:
	for i, l in enumerate(seq):
		P[l][i] += 1
c = ''
for l in range(seq_len):
	C = 0, 'N'
	for key in P.keys():
		if P[key][l] > C[0]:
			C = P[key][l], key
	c += C[1]
print c
for key in 'ACGT':
	print key + ': ' + ' '.join([ str(x) for x in P[key]])

