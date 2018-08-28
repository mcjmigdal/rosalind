from operator import mul
n = 890590
s = "CCATAATTCC"
A = "0.000 0.119 0.182 0.242 0.277 0.327 0.381 0.451 0.559 0.612 0.636 0.689 0.793 0.865 0.919 1.000"
A = [ float(a) for a in A.split() ]
def f(x):
	return { "A" : (1-x)/2, "G" : x/2, "C" : x/2, "T" : (1-x)/2 }
B = []
for p in A:
	ps = reduce(mul, [f(p)[letter] for letter in s], 1)
	B.append( round(ps * (n - len(s) +1), 3 ) )
print " ".join([ str(b) for b in B])	
