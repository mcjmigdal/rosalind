from Bio.Seq import Seq
from Bio.Alphabet.IUPAC import unambiguous_rna
from sys import argv

inp = open(argv[1]).readline().strip()
s = Seq(inp,unambiguous_rna)
print s.translate(to_stop=True)
