def draw(piece,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb):
	from possiblemove import possiblemove
	from opencheck import opencheck 
	pm=[]
	pmt=[]
	z=0	
	if piece[0]=='B':
		for i1 in wpiece:
			i=i1[0]
			pm=possiblemove(i,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)			
			pm=opencheck(pm,i,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb)
			if pm!=[]:
				z=1		
		if z==1:			
			pmt.append(pm)
		else:
			pmt=[]	
		if pmt==[]:
			print("Game Draw")
			print("press any key to quit")
			abc=input()
			exit()
	if piece[0]=='W':
		for i1 in bpiece:
			i=i1[0]
			pm=possiblemove(i,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)			
			pm=opencheck(pm,i,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb)
			if pm!=[]:
				z=1					
		if z==1:			
			pmt.append(pm)
		else:
			pmt=[]
		if pmt==[]:
			print("Game Draw")
			print("press any key to quit")
			abc=input()
			exit()

