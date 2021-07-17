def opencheck(pmove,piece,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb):
	from makemove import makemove 
	import copy
	if piece[0]=='W':
		x=wpiece[12][1]
		for i in range(8):
			for j in range(8):
				if x==cmove[i][j]:
					p=i
					q=j
	else:
		x=bpiece[12][1]
		for i in range(8):
			for j in range(8):
				if x==cmove[i][j]:
					p=i
					q=j
	zmove=[]
	for k in pmove:
		aboard=copy.deepcopy(board)
		bwpiece=copy.deepcopy(wpiece)
		bbpiece=copy.deepcopy(bpiece)
		aboard=makemove(piece,k,aboard,bwpiece,bbpiece,kwmove,kbmove,cmove,prw,prb)
		oc=0
		a=p+1
		b=q+1	
		while (a in range(8)) and (b in range(8)) and ((aboard[a][b]=="///") or (aboard[a][b]=="   ")):
			a+=1
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='B':
				if aboard[a][b][0]=='W':
					if (aboard[a][b][1]=='B') or (aboard[a][b][1]=='Q'):
						oc=1
			else:
				if aboard[a][b][0]=='B':
					if (aboard[a][b][1]=='B') or (aboard[a][b][1]=='Q'):
						oc=1	
		a=p+1
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((aboard[a][b]=="///") or (aboard[a][b]=="   ")):
			a+=1
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='B':
				if aboard[a][b][0]=='W':
					if (aboard[a][b][1]=='B') or (aboard[a][b][1]=='Q'):
						oc=1
			else:
				if aboard[a][b][0]=='B':
					if (aboard[a][b][1]=='B') or (aboard[a][b][1]=='Q'):
						oc=1
		a=p-1
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((aboard[a][b]=="///") or (aboard[a][b]=="   ")):
			a-=1
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='B':
				if aboard[a][b][0]=='W':
					if (aboard[a][b][1]=='B') or (aboard[a][b][1]=='Q'):
						oc=1
			else:
				if aboard[a][b][0]=='B':
					if (aboard[a][b][1]=='B') or (aboard[a][b][1]=='Q'):
						oc=1
		a=p-1
		b=q+1
		while (a in range(8)) and (b in range(8)) and ((aboard[a][b]=="///") or (aboard[a][b]=="   ")):
			a-=1
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='B':
				if aboard[a][b][0]=='W':
					if (aboard[a][b][1]=='B') or (aboard[a][b][1]=='Q'):
						oc=1
			else:
				if aboard[a][b][0]=='B':
					if (aboard[a][b][1]=='B') or (aboard[a][b][1]=='Q'):
						oc=1
		a=p+1
		b=q	
		while (a in range(8)) and (b in range(8)) and ((aboard[a][b]=="///") or (aboard[a][b]=="   ")):
			a+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='B':
				if aboard[a][b][0]=='W':
					if (aboard[a][b][1]=='R') or (aboard[a][b][1]=='Q'):
						oc=1
			else:
				if aboard[a][b][0]=='B':
					if (aboard[a][b][1]=='R') or (aboard[a][b][1]=='Q'):
						oc=1
		a=p-1
		b=q
		while (a in range(8)) and (b in range(8)) and ((aboard[a][b]=="///") or (aboard[a][b]=="   ")):
			a-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='B':
				if aboard[a][b][0]=='W':
					if (aboard[a][b][1]=='R') or (aboard[a][b][1]=='Q'):
						oc=1
			else:
				if aboard[a][b][0]=='B':
					if (aboard[a][b][1]=='R') or (aboard[a][b][1]=='Q'):
						oc=1
		a=p
		b=q+1
		while (a in range(8)) and (b in range(8)) and ((aboard[a][b]=="///") or (aboard[a][b]=="   ")):
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='B':
				if aboard[a][b][0]=='W':
					if (aboard[a][b][1]=='R') or (aboard[a][b][1]=='Q'):
						oc=1
			else:
				if aboard[a][b][0]=='B':
					if (aboard[a][b][1]=='R') or (aboard[a][b][1]=='Q'):
						oc=1
		a=p
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((aboard[a][b]=="///") or (aboard[a][b]=="   ")):
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='B':
				if aboard[a][b][0]=='W':
					if (aboard[a][b][1]=='R') or (aboard[a][b][1]=='Q'):
						oc=1
			else:
				if aboard[a][b][0]=='B':
					if (aboard[a][b][1]=='R') or (aboard[a][b][1]=='Q'):
							oc=1
		if oc==1:
			zmove.append(k)
	for l in zmove:
		pmove.remove(l)
	return (pmove)
			
