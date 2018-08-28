#http://www.keithschwarz.com/interesting/code/knuth-morris-pratt/KnuthMorrisPratt.python.html

def failTable(pattern):
	result = [None]

	for i in range(0, len(pattern)):
		j = i

		while True:
			if j == 0:
				result.append(0)
				break
			if pattern[result[j]] == pattern[i]:
				result.append(result[j] + 1)
				break
			
			j = result[j]
	return result

def kmpMatch(needle, haystack):
	fail = failTable(needle)
	index = 0
	match = 0

	while index + match < len(haystack):
		if haystack[index + match] == needle[match]:
			match = match + 1
			if match == len(needle):
				return index
		else:
			if match == 0:
				index += 1
			else:
				index = index + match - fail[match]
				match = fail[match]
	return None

def readFasta(path):
	Seq = []
	with open(path) as inp:
		s = ''
		line = inp.readline().strip()
		while line:
			line = inp.readline().strip()
			if line.startswith('>'):
				Seq.append(s)
				s = ''
			else:
				s += line
		Seq.append(s)
	return Seq

def genMotif(s,length):
	stimes = len(s) - length
	motifs = []
	for i in range(stimes+1):
		motifs.append( s[i:i+length] )
	return motifs

from sys import argv
sequences = readFasta(argv[1])
lmotif = len(sequences[0])
HIT = len(sequences[1:])
while lmotif > 1:
	motifs = genMotif(sequences[0],lmotif)
	hit = 0
	for mot in motifs:
		#if not kmpMatch(mot,seq):	
		if all(seq.find(mot) == -1 for seq in sequences[1:]):
		#if not mot in seq:
			hit = 0
			break
		else:
			hit += 1
		if hit == HIT:
			print mot
			lmotif = 1
			break
	lmotif -= 1
