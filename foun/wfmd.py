from __future__ import division
from math import *
import numpy as np

def Bin(n,k,p):
	return factorial(n)/factorial(k)/factorial(n-k) * p**k * (1-p)**(n-k)

N, m = 4, 3
A = [ int(a) for a in raw_input("matrix : ").split() ]
T = []
for i in range(2*N+1):
	T.append( [Bin(2*N,j,i/2/N) for j in range(2*N+1)] )

T = np.array(T)
for a in A:
	v = np.zeros(2*N+1)
	v[2*N - a] = 1
	for i in range(m):
		v = v.dot(T)
		if v[0] == 0.0:
			print v[0]
		else:
			print log(v[0],10)
