from math import *
def Bin(k,n,p=0.5):
	return (factorial(n)/factorial(k)/factorial(n-k)) * p**k * (1-p)**(n-k)

n = input()
i = range(1,(2*n+1))
o = []
for k in i:
	o.append( round( log( sum([ Bin(kk,2*n) for kk in range(k,2*n+1) ]), 10 ), 3) )

print " ".join([ str(num) for num in o])
