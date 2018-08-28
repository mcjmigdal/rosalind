s='''>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG'''

from sys import argv
with open(argv[1]) as inp:
	s = inp.read().strip()

Seq = s.split('>')
Seq = [ (s.split('\n')[0],''.join(s.split('\n')[1:])) for s in Seq[1:] ]
out = []

for i, s in enumerate(Seq):
	for z in Seq[:i] + Seq[i+1:]:
		if s[1][:3] == z[1][-3:] and s != z:
			print z[0], s[0]
