from __future__ import division
from math import factorial
import numpy as np

def Bin(n,k,p):
	return factorial(n)/factorial(k)/factorial(n-k) * p**k * (1-p)**(n-k)

N, m, g, k = 4, 6, 2, 1
T = []
for i in range(2*N+1):
	T.append( [Bin(2*N,j,i/2/N) for j in range(2*N+1)] )

T = np.array(T)
v = np.zeros(2*N+1)
v[2*N - m] = 1
for i in range(g):
	v = v.dot(T)
print sum(v[k:])
#p = 1 - m/2/N
#for i in range(g):
#	print p
#	p = sum([ Bin(2*N,i,p) for i in range(k,2*N+1) ])	

#from numpy.random import choice
#S = 0
#it=100000
#for i in range(it):
#	p = m/2/N
#	q = 1 - p
#	for i in range(g):
#		P = choice([0,1],2*N,p=[p,q]) # 1-generation
#		p = (2*N - sum(P)) / 2 / N
#		q = 1 - p 
#	# if there is 1 or more than we have success
#	if sum(P) >= k:
#		S += 1
#print S/it

# number of successes / iterations
