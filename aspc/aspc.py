from math import factorial
def C(n,k):
	return factorial(n)/factorial(k)/factorial(n-k)

n, m = input('type numbers : ')
print  sum([ C(n,k) for k in range(m,n+1) ]) % 1000000
