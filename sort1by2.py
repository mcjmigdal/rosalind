#!/usr/bin/env python2.7
#By Migdal Warsaw Central Station

def sortAbyB0(A,B):
	'''A = [ [a,b], .. ], B=[ [a,c], .. ]'''
	size = len(B)
	Asorted = []
	for i in xrange(size):
		for j in xrange(len(A)):
			if B[i][0] in A[j][0] or A[j][0] in B[i][0]:
				Asorted.append(A[j])
				A.pop(j)
				break
	A += Asorted

if __name__ == '__main__':
	A = [ ['a',5], ['b',2], ['c',1], ['d',7], ['e',15] ]
	B = [ ['d',5], ['e',2], ['a',1], ['b',7], ['c',15] ]
	print ' list A:', A, ' \n list B:', B
	sortAbyB0(B,A)
	print 'list B\':', B
	if ''.join([ x[0] for x in B]) == 'abcde': print 'sucess'
		
