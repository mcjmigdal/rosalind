#!/usr/bin/python
#pi = (0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15)
pi = (8, 2, 1, 6, 5, 7, 4, 3, 9)
n = len(pi)

def lgis(n, pi):
	S = [[]] * (n+1)
	for i in pi:
		S[i] = max(S[:i], key=len) + [i]
		print S

	return ' '.join(map(str, max(S, key=len) ) )

print lgis(n,pi)
print lgis(n, reversed(pi))[::-1]
