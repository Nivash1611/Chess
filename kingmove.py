def kingmove(piece,pmove,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb):
	from makemove import makemove
	import copy
	zmove=[]
	for k in pmove:
		w=wpiece
		b=bpiece
		for i in range(8):
			for j in range(8):
				if k==cmove[i][j]:
					p=i
					q=j
		aboard=copy.deepcopy(board)
		awpiece=copy.deepcopy(wpiece)
		abpiece=copy.deepcopy(bpiece)
		aboard=makemove(piece,k,aboard,awpiece,abpiece,kwmove,kbmove,cmove,prw,prb)
		wpiece=w
		bpiece=b
		a=p+1
		b=q+1
		oc=0	
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
		if piece[0]=='W':
			if (p-1 in range(8)) and (q-1 in range(8)):
				if (aboard[p-1][q-1][0]=='B') and (aboard[p-1][q-1][1]=='P'):
					oc=1
			if (p-1 in range(8)) and (q+1 in range(8)):
				if (aboard[p-1][q+1][0]=='B') and (aboard[p-1][q+1][1]=='P'):
					oc=1
		if piece[0]=='B':
			if (p+1 in range(8)) and (q-1 in range(8)):
				if (aboard[p+1][q-1][0]=='W') and (aboard[p+1][q-1][1]=='P'):
					oc=1
			if (p+1 in range(8)) and (q+1 in range(8)):
				if (aboard[p+1][q+1][0]=='W') and (aboard[p+1][q+1][1]=='P'):
					oc=1
		if (p+1 in range(8)) and (q in range(8)):
			if (aboard[p+1][q][2]=='K'):
		 		oc=1
		if (p+1 in range(8)) and (q+1 in range(8)):
			if (aboard[p+1][q+1][2]=='K'):
				oc=1
		if (p+1 in range(8)) and (q-1 in range(8)):
			if (aboard[p+1][q-1][2]=='K'):
				oc=1
		if (p in range(8)) and (q+1 in range(8)):
			if (aboard[p][q+1][2]=='K'):
				oc=1
		if (p in range(8)) and (q-1 in range(8)):
			if (aboard[p][q-1][2]=='K'):
				oc=1
		if (p-1 in range(8)) and (q in range(8)):
			if (aboard[p-1][q][2]=='K'):
				oc=1
		if (p-1 in range(8)) and (q+1 in range(8)):
			if (aboard[p-1][q+1][2]=='K'):
				oc=1
		if (p-1 in range(8)) and (q-1 in range(8)):
			if (aboard[p-1][q-1][2]=='K'):
				oc=1
		if piece[0]=='W':
			if (p+1 in range(8)) and (q+2 in range(8)):
				if (aboard[p+1][q+2][0]=="B") and (aboard[p+1][q+2][1]=="K"):
					oc=1
			if (p+1 in range(8)) and (q-2 in range(8)):
				if (aboard[p+1][q-2][0]=='B') and (aboard[p+1][q-2][1]=="K"):
					oc=1
			if (p-1 in range(8)) and (q+2 in range(8)):
				if (aboard[p-1][q+2][0]=='B') and (aboard[p-1][q+2][1]=="K"):
					oc=1
			if (p-1 in range(8)) and (q-2 in range(8)):
				if (aboard[p-1][q-2][0]=='B') and (aboard[p-1][q-2][1]=="K"):
					oc=1
			if (p+2 in range(8)) and (q+1 in range(8)):
				if (aboard[p+2][q+1][0]=='B') and (aboard[p+2][q+1][1]=="K"):
					oc=1
			if (p+2 in range(8)) and (q-1 in range(8)):
				if (aboard[p+2][q-1][0]=='B') and (aboard[p+2][q-1][1]=="K"):
					oc=1
			if (p-2 in range(8)) and (q+1 in range(8)):
				if (aboard[p-2][q+1][0]=='B') and (aboard[p-2][q+1][1]=="K"):
					oc=1
			if (p-2 in range(8)) and (q-1 in range(8)):
				if (aboard[p-2][q-1][0]=='B') and (aboard[p-2][q-1][1]=="K"):
					oc=1
		if piece[0]=='B':
			if (p+1 in range(8)) and (q+2 in range(8)):
				if (aboard[p+1][q+2][0]=="W") and (aboard[p+1][q+2][1]=="K"):
					oc=1
			if (p+1 in range(8)) and (q-2 in range(8)):
				if (aboard[p+1][q-2][0]=='W') and (aboard[p+1][q-2][1]=="K"):
					oc=1
			if (p-1 in range(8)) and (q+2 in range(8)):
				if (aboard[p-1][q+2][0]=='W') and (aboard[p-1][q+2][1]=="K"):
					oc=1
			if (p-1 in range(8)) and (q-2 in range(8)):
				if (aboard[p-1][q-2][0]=='W') and (aboard[p-1][q-2][1]=="K"):
					oc=1
			if (p+2 in range(8)) and (q+1 in range(8)):
				if (aboard[p+2][q+1][0]=='W') and (aboard[p+2][q+1][1]=="K"):
					oc=1
			if (p+2 in range(8)) and (q-1 in range(8)):
				if (aboard[p+2][q-1][0]=='W') and (aboard[p+2][q-1][1]=="K"):
					oc=1
			if (p-2 in range(8)) and (q+1 in range(8)):
				if (aboard[p-2][q+1][0]=='W') and (aboard[p-2][q+1][1]=="K"):
					oc=1
			if (p-2 in range(8)) and (q-1 in range(8)):
				if (aboard[p-2][q-1][0]=='W') and (aboard[p-2][q-1][1]=="K"):
					oc=1
		if oc==1:
			zmove.append(k)
	for l in zmove:
		pmove.remove(l)
	return pmove
