# I think its invert of lcsq problem using highest vaoted rosalind solution
# for lcsq it look like this
from Bio import SeqIO

A, B = [ str(fa.seq) for fa in SeqIO.parse('edit.txt', 'fasta') ]
cur = [''] * (len(B) + 1)
for a in A:
    last, cur = cur, ['']
    for i, b in enumerate(B):
        cur.append(last[i] + a if a == b else max(last[i+1], cur[-1], key=len))

print len(A), len(B), len(cur[-1])
print len(cur[-1])
