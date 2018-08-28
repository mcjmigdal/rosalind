import random

k,n,m = 17, 17, 26
result = 0
r = 40000000
for i in xrange(r):
	kk, nn, mm = k, n, m
	P = ['AA'] * k + ['Aa'] * n + ['aa'] * m
	a = ''
	a += random.choice(P)
	P.remove(a)
	a += random.choice(P)
	if a[:2] == 'AA' or a[-2:] == 'AA':
		result += 1
	elif ( a[:2] == 'Aa' and a[-2:] == 'Aa' ) and random.random() > 0.25:
		result += 1
	elif a.count('A') == 1 and random.random() > 0.5:
		result += 1
	else:
		pass
print result/float(r)
	
