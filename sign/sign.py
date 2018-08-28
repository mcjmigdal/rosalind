#!/usr/bin/python2.7
# Warsaw 12/11/17
# Rosalind sign
# Problem:
# Given: A positive integer n<=6.
# Return: The total number of signed permutations of length nn, followed by a list of all such permutations (you may list the signed permutations in any order).
from math import factorial

def permutations(A):
	if len(A) <= 1:
		yield A
	else:
		for perm in permutations(A[1:]):
			for i in range(len(A)):
				yield perm[:i] + A[0:1] + perm[i:]

def choose(N,k):
	if k <= 0:
		yield []
	elif k == 1:
		for n in N:
			yield [n]
	else:
		for i in range(len(N)-k+1):
			for ch in choose(N[i+1:], k-1):
				yield [N[i]] + ch

A = [ 1, 2, 3, 4, 5 ]
print 2**len(A) * factorial(len(A))
for k in range(len(A)+1):
	for idx in choose(range(len(A)),k):
		for i in idx: 
			A[i] *= -1
		for perm in permutations(A): print " ".join([ str(p) for p in perm])
		for j in range(len(A)):
			if A[j] < 0: 
				A[j] *= -1
