def checkmate(piece,board,wpiece,bpiece,prw,prb,cpiece,cmove,kwmove,kbmove):
	from possiblemove import possiblemove
	from blockcheck import blockcheck
	from opencheck import opencheck
	pmt=[]
	Z4=0
	z=0	
	for j4 in cpiece:
		Z4+=1
	if Z4==1:
		if piece[0]=='W':
			for i1 in wpiece:
				i=i1[0]				
				pm=[]
				pm=possiblemove(i,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
				pm=blockcheck(cpiece,i,pm,board,wpiece,bpiece,cmove)
				pm=opencheck(pm,i,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb)
				if pm!=[]:		
					z=1
			if z==1:			
				pmt.append(pm)
			else:
				pmt=[]
			if pmt==[]:
				print("CHECKMATE ")
				print("Player 1 Won The Game")
				print("press any key to quit")
				abc=input()
				exit()
		if piece[0]=='B':
			for i1 in bpiece:
				i=i1[0]				
				pm=[]
				pm=possiblemove(i,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
				pm=blockcheck(cpiece,i,pm,board,wpiece,bpiece,cmove)
				pm=opencheck(pm,i,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb)
				if pm!=[]:		
					z=1
			if z==1:			
				pmt.append(pm)
			else:
				pmt=[]
			if pmt==[]:
				print("CHECKMATE ")
				print("Player 2 Won The Game")
				print("press any key to quit")
				abc=input()
				exit()
	else:
		if piece[0]=='W':
			print("CHECKMATE ")
			print("Player 1 Won The Game")
			print("press any key to quit")
			abc=input()
			exit()
		if piece[0]=='B':
			print("CHECKMATE ")
			print("Player 2 Won The Game")
			print("press any key to quit")
			abc=input()
			exit()
			
			
