n = input('give n: ')
P = raw_input("give p's: ")
P = [ float(p) for p in P.split() ]
print " ".join([ str(p*n) for p in P])
