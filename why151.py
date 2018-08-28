#!/usr/bin/python2.7
from random import randint

def globalAlign(ref,seq,MM=0):
	hit = []
	slen = len(seq)
	for i in xrange(0,len(ref)-slen+1):
		count = 0
		for j,k in enumerate(seq):
			if ref[i+j] == k:
				count += 1
		if (count + MM) >= slen:
			hit.append( i )
	for a in hit:
#		print ref
#		print ' '*a + seq + '\n'
#
		return 1
	return 0
#'AA'
#'AA','AT','TT','TA'
#'AATTA'
#'AAA'
#'AAA','AAT','ATT','TTT','ATA','TTA','TAA','TAT'
#'AAATTTAATAT'
from sys import argv
if len(argv) != 3:
	print 'Usage: seq_len MM'

slen = int(argv[1])
MM = int(argv[2])
seq = ''.join(['A' for i in range(slen)])
choice = 'A'
C = len(choice)
L = len(seq)
ref = set()
while len(ref) < C**L:
	k = ''
	for i in xrange(L):
		k += choice[randint(0,C-1)]	
	ref.update([k])

count = 0
for r in ref:
	count += globalAlign(r,seq,MM=MM)
print count
