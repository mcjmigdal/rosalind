from operator import mul
from math import log
from math import exp
N = 85372
GC = 0.588557
alphabet = { "A" : (1-GC)/2, "G" : GC/2, "C" : GC/2, "T" : (1-GC)/2 }
# p of generating sequence M == prod( p(M[i]) for i in M )
# p of not generating any sequence is 1-p(generate M), then p of generating at least one is
# 1 - (1 - p(generate M))^N
motif = "ATTCCGAA"
p_gen_M = log( 1 - reduce( mul, [ alphabet[m] for m in motif ], 1 ) )
p_not_gen_M = 0
for i in range(N-1):
	p_not_gen_M += p_gen_M
print round(1 - exp(p_not_gen_M), 3)
