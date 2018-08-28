from Bio import SeqIO
fasta = [ fa for fa in SeqIO.parse('corr.txt', 'fasta') ]

def one(a,b):
	la = len(a)
	idx = range( len(a) )
	a, arev, b, brev = a.seq, a.reverse_complement().seq, b.seq, b.reverse_complement().seq
	if sum([ a[i] == b[i] for i in idx]) == la - 1:
		return a, b
	elif sum([ arev[i] == b[i] for i in idx]) == la - 1:
		return arev, b
	elif sum([ a[i] == brev[i] for i in idx]) == la - 1:
		return a, brev 
	elif sum([ arev[i] == b[i] for i in idx]) == la - 1:
		return arev, brev
	else:
		return False, False

def corr(a,b):
	s = b + "->" + a
	print s
		

# Group same reads into bins
grouped = []
for i in range(len(fasta)):
	if i in grouped:
		continue
	n = 1
	g = [i]
	for j in range(len(fasta)):
		if j in grouped:
			continue
		a, arev, b, brev = fasta[i].seq, fasta[i].reverse_complement().seq, fasta[j].seq, fasta[j].reverse_complement().seq
		if j != i and (a == b or arev == brev or a == brev or arev == b):
			g.append(j)
	if len(g) > 1:
		grouped += g

uncor = [ idx for idx in range(len(fasta)) if idx not in grouped ]
for i in uncor:
	for j in grouped:
		a, b = one(fasta[j], fasta[i])
		if b:
			corr(a, b)
			break
