from Bio import SeqIO
from math import factorial
fasta = SeqIO.read("pmch.txt", "fasta")
na = sum([ 1 for l in fasta.seq if l == 'A' ])
ng = sum([ 1 for l in fasta.seq if l == 'G' ])
pa = reduce(lambda x, y: x*y, [ i for i in range(1,na+1) ])
pg = reduce(lambda x, y: x*y, [ i for i in range(1,ng+1) ])
print pa * pg
