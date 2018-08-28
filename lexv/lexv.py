A = [ "", "V", "K", "A", "B", "T", "Q", "P", "M", "L", "I" ]
N = 3
def f(length, word):
	if length == N:
		if not any([ word[i-1] == "" and word[i] in A[1:] for i in range(1,N) ]):
			print "".join(word)
		return
	else:
		for a in A:
			f(length + 1, word + [a])
f(0,[])
