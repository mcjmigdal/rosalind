from Bio import SeqIO
fasta = SeqIO.parse("sseq.fa", "fasta")
a = fasta.next().seq
b = fasta.next().seq
sol = []
j = 0
for i in range( len(a) ):
	if a[i] == b[j] and j < len(b):
		sol.append(i + 1)
		j += 1
	if j >= len(b): break

if len(sol) == len(b):
	print sol
 
