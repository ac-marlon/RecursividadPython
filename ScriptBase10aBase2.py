bDiez=input()

def convB2(bDiez):
	if bDiez==0: return 0
	if bDiez==1: return 1
	if bDiez>2: return convB2(bDiez%2)
	print bDiez
