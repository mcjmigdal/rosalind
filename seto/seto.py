#!/usr/bin/python2.7
data = open("seto.txt")
U = int(data.readline().strip())
U = set(range(1,U+1))
A = data.readline().strip().strip("{}")
A = set([ int(a) for a in A.split(',') ])
B = data.readline().strip().strip("{}")
B = set([ int(b) for b in B.split(',') ])

print "{" + ", ".join([ str(e) for e in A.union(B)]) + "}"
print "{" + ", ".join([ str(e) for e in A.intersection(B)]) + "}"
print "{" + ", ".join([ str(e) for e in A.difference(B)]) + "}"
print "{" + ", ".join([ str(e) for e in B.difference(A)]) + "}"
print "{" + ", ".join([ str(e) for e in U.difference(A)]) + "}"
print "{" + ", ".join([ str(e) for e in U.difference(B)]) + "}"
