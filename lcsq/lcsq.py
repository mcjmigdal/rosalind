from Bio import SeqIO
import numpy as np

a, b = [ str(fa.seq) for fa in SeqIO.parse('lcsq.txt', 'fasta') ]
def LCS(a,b):
    C = np.zeros((len(a)+1, len(b)+1))
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                C[i,j] = C[i-1, j-1] + 1
            else:
                C[i, j] = max(C[i, j-1], C[i-1, j])
    lcs = ""
    i, j = len(a), len(b)
    while True:
        if i == 0 or j == 0:
            return lcs[::-1]
        elif a[i-1] == b[j-1]:
            lcs += a[i-1]
            i, j = i - 1, j - 1
        elif C[i, j-1] > C[i-1,j]:
            j -= 1
        else:
            i -= 1

print LCS(a,b)
