def Fibbonachi(n=85,k=1,d=18):
	F = [ 1, 1 ]
	while n > 1:
		if len(F) == d:
			F.append( F[-1] + k*F[-2] - 1 )
		elif len(F) > d:
			F.append( F[-1] + k*F[-2] - F[-d-1] )
		else:
			F.append(F[-1] + k*F[-2])
		n -= 1
	print F

Fibbonachi()
