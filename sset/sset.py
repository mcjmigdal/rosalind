#!/usr/bin/python2.7
from math import factorial

def choose(n,k):
	return factorial(n) / (factorial(k) * factorial(n-k))

n = 954
s = 0
for k in range(n+1):
	s += choose(n, k) 

print s	% 1000000
