from Bio import SeqIO

def splice(premrna, intron):
	ilen = len(intron)
	for i in range( len(premrna) - ilen ):
		if premrna[i:i+ilen] == intron:
			return premrna[:i] + premrna[i+ilen:]
	return premrna

fasta = SeqIO.parse("splc.fa", "fasta")
template = fasta.next().seq
for f in fasta:
	template = splice(template, f.seq)

print template.translate()
