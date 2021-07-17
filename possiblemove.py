def possiblemove(piece,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb):
	from kingmove import kingmove
	pmove=[]
	if piece[1]=='P':	
		if piece[0]=='W':
			for i in range(8):
				if piece==wpiece[i][0]:
					x=wpiece[i][1]
			for i in range(8):
				for j in range(8):
					if x==cmove[i][j]:
						p=i
						q=j
			if x[1]=='2':
				if (board[p-1][q]=='///') or (board[p-1][q]=='   '):
					if (board[p-2][q]=='///') or (board[p-2][q]=='   '):
						pmove=[cmove[p-1][q],cmove[p-2][q]]
					else:
						pmove=[cmove[p-1][q]]
			else:
				if (board[p-1][q]=='///') or (board[p-1][q]=='   '):
					pmove=[cmove[p-1][q]]
			if ((p-1 in range(8)) and (q-1 in range(8))):
				if (board[p-1][q-1][0]=='B'):
					pmove.append(cmove[p-1][q-1])
			if ((p-1 in range(8)) and (q+1 in range(8))):
				if (board[p-1][q+1][0]=='B'):
					pmove.append(cmove[p-1][q+1])

		else: 	
			for i in range(8):
				if piece==bpiece[i][0]:
					x=bpiece[i][1]
			for i in range(8):
				for j in range(8):
					if x==cmove[i][j]:
						p=i
						q=j
			if x[1]=='7':
				if (board[p+1][q]=='///') or (board[p+1][q]=='   '):
					if (board[p+2][q]=='///') or (board[p+2][q]=='   '):
						pmove=[cmove[p+1][q],cmove[p+2][q]]
					else:
						pmove=[cmove[p+1][q]]
			else:
				if (board[p+1][q]=='///') or (board[p+1][q]=='   '):
					pmove=[cmove[p+1][q]]
			if ((p+1 in range(8)) and (q+1 in range(8))):
				if (board[p+1][q+1][0]=='W'):
					pmove.append(cmove[p+1][q+1])
			if ((p+1 in range(8)) and (q-1 in range(8))):
				if (board[p+1][q-1][0]=='W'):
					pmove.append(cmove[p+1][q-1])
	if piece[1]=='B':
		if piece[0]=='W':
			if piece[2]=='1':
				x=wpiece[10][1]
			elif piece[2]=='2':
				x=wpiece[13][1]
			else:
				for d in range(8):
					if piece==wpiece[d][0]:
						x=wpiece[d][1]
		if piece[0]=='B':
			if piece[2]=='1':
				x=bpiece[10][1]
			elif piece[2]=='2':
				x=bpiece[13][1]
			else:
				for d in range(8):
					if piece==bpiece[d][0]:
						x=bpiece[d][1]
		for i in range(8):
			for j in range(8):
				if cmove[i][j]==x:
					p=i
					q=j
		a=p+1
		b=q+1	
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a+=1
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p+1
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a+=1
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p-1
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a-=1
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p-1
		b=q+1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a-=1
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
	if piece[1]=='K':
		if piece[0]=='W':
			if piece[2]=='1':
				x=wpiece[9][1]
			elif piece[2]=='2':
				x=wpiece[14][1]
			else:
				for d in range(8):
					if piece==wpiece[d][0]:
						x=wpiece[d][1]
			for i in range(8):
				for j in range(8):
					if x==cmove[i][j]:
						p=i
						q=j
			if (p+1 in range(8)) and (q+2 in range(8)):
				if (board[p+1][q+2][0] not in ['W']):
					pmove.append(cmove[p+1][q+2])
			if (p+1 in range(8)) and (q-2 in range(8)):
				if (board[p+1][q-2][0] not in ['W']):
					pmove.append(cmove[p+1][q-2])
			if (p-1 in range(8)) and (q+2 in range(8)):
				if (board[p-1][q+2][0] not in ['W']):
					pmove.append(cmove[p-1][q+2])
			if (p-1 in range(8)) and (q-2 in range(8)):
				if (board[p-1][q-2][0] not in ['W']):
					pmove.append(cmove[p-1][q-2])
			if (p+2 in range(8)) and (q+1 in range(8)):
				if (board[p+2][q+1][0] not in ['W']):
					pmove.append(cmove[p+2][q+1])
			if (p+2 in range(8)) and (q-1 in range(8)):
				if (board[p+2][q-1][0] not in ['W']):
					pmove.append(cmove[p+2][q-1])
			if (p-2 in range(8)) and (q+1 in range(8)):
				if (board[p-2][q+1][0] not in ['W']):
					pmove.append(cmove[p-2][q+1])
			if (p-2 in range(8)) and (q-1 in range(8)):
				if (board[p-2][q-1][0] not in ['W']):
					pmove.append(cmove[p-2][q-1])
		if piece[0]=='B':
			if piece[2]=='1':
				x=bpiece[9][1]
			elif piece[2]=='2':		
				x=bpiece[14][1]
			else:
				for d in range(8):
					if piece==bpiece[d][0]:
						x=bpiece[d][1]
			for i in range(8):
				for j in range(8):
					if x==cmove[i][j]:
						p=i
						q=j
			if (p+1 in range(8)) and (q+2 in range(8)):
				if (board[p+1][q+2][0] not in ['B']):
					pmove.append(cmove[p+1][q+2])
			if (p+1 in range(8)) and (q-2 in range(8)):
				if (board[p+1][q-2][0] not in ['B']):
					pmove.append(cmove[p+1][q-2])
			if (p-1 in range(8)) and (q+2 in range(8)):
				if (board[p-1][q+2][0] not in ['B']):
					pmove.append(cmove[p-1][q+2])
			if (p-1 in range(8)) and (q-2 in range(8)):
				if (board[p-1][q-2][0] not in ['B']):
					pmove.append(cmove[p-1][q-2])
			if (p+2 in range(8)) and (q+1 in range(8)):
				if (board[p+2][q+1][0] not in ['B']):
					pmove.append(cmove[p+2][q+1])
			if (p+2 in range(8)) and (q-1 in range(8)):
				if (board[p+2][q-1][0] not in ['B']):
					pmove.append(cmove[p+2][q-1])
			if (p-2 in range(8)) and (q+1 in range(8)):
				if (board[p-2][q+1][0] not in ['B']):
					pmove.append(cmove[p-2][q+1])
			if (p-2 in range(8)) and (q-1 in range(8)):
				if (board[p-2][q-1][0] not in ['B']):
					pmove.append(cmove[p-2][q-1])
	if piece[1]=='R':
		if piece[0]=='W':
			if piece[2]=='1':
				x=wpiece[8][1]
			elif piece[2]=='2':
				x=wpiece[15][1]
			else:
				for d in range(8):
					if piece==wpiece[d][0]:
						x=wpiece[d][1]
		else:
			if piece[2]=='1':
				x=bpiece[8][1]
			elif piece[2]=='2':
				x=bpiece[15][1]
			else:
				for d in range(8):
					if piece==bpiece[d][0]:
						x=bpiece[d][1]	
		for i in range(8):
			for j in range(8):
				if cmove[i][j]==x:
					p=i
					q=j
		a=p+1
		b=q	
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p-1
		b=q
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p
		b=q+1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:	
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
	if piece[1]=='Q':
		if piece[0]=='W':
			if piece[2]=='1':
				x=wpiece[11][1]
			else:
				for d in range(8):
					if piece==wpiece[d][0]:
						x=wpiece[d][1]
		if piece[0]=='B':
			if piece[2]=='1':
				x=bpiece[11][1]
			else:
				for d in range(8):
					if piece==bpiece[d][0]:
						x=bpiece[d][1]
		for i in range(8):
			for j in range(8):
				if cmove[i][j]==x:
					p=i
					q=j
		a=p+1
		b=q+1	
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a+=1
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p+1
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a+=1
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p-1
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a-=1
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p-1
		b=q+1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a-=1
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p+1
		b=q	
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p-1
		b=q
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			a-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p
		b=q+1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			b+=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
		a=p
		b=q-1
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			pmove.append(cmove[a][b])
			b-=1
		if (a in range(8)) and (b in range(8)):
			if piece[0]=='W':
				if board[a][b][0]=='B':
					pmove.append(cmove[a][b])
			else:
				if board[a][b][0]=='W':
					pmove.append(cmove[a][b])
	if piece[2]=="K":
		if piece[0]=='W':
			x=wpiece[12][1]
		if piece[0]=='B':
			x=bpiece[12][1]
		for i in range(8):
			for j in range(8):
				if cmove[i][j]==x:
					p=i
					q=j
		if (p+1 in range(8)) and (q in range(8)) and ((board[p+1][q]=="///") or (board[p+1][q]=="   ")):
			pmove.append(cmove[p+1][q])
		if (p+1 in range(8)) and (q in range(8)):
			if piece[0]=='W':
				if board[p+1][q][0]=='B':
					pmove.append(cmove[p+1][q])
			else:
				if board[p+1][q][0]=='W':
					pmove.append(cmove[p+1][q])
		if (p+1 in range(8)) and (q+1 in range(8)) and ((board[p+1][q+1]=="///") or (board[p+1][q+1]=="   ")):
			pmove.append(cmove[p+1][q+1])
		if (p+1 in range(8)) and (q+1 in range(8)):
			if piece[0]=='W':
				if board[p+1][q+1][0]=='B':
					pmove.append(cmove[p+1][q+1])
			else:
				if board[p+1][q+1][0]=='W':
					pmove.append(cmove[p+1][q+1])
		if (p in range(8)) and (q+1 in range(8)) and ((board[p][q+1]=="///") or (board[p][q+1]=="   ")):
			pmove.append(cmove[p][q+1])
		if (p in range(8)) and (q+1 in range(8)):
			if piece[0]=='W':
				if board[p][q+1][0]=='B':
					pmove.append(cmove[p][q+1])
			else:
				if board[p][q+1][0]=='W':
					pmove.append(cmove[p][q+1])
		if (p-1 in range(8)) and (q+1 in range(8)) and ((board[p-1][q+1]=="///") or (board[p-1][q+1]=="   ")):
			pmove.append(cmove[p-1][q+1])
		if (p-1 in range(8)) and (q+1 in range(8)):
			if piece[0]=='W':
				if board[p-1][q+1][0]=='B':
					pmove.append(cmove[p-1][q+1])
			else:
				if board[p-1][q+1][0]=='W':
					pmove.append(cmove[p-1][q+1])
		if (p-1 in range(8)) and (q in range(8)) and ((board[p-1][q]=="///") or (board[p-1][q]=="   ")):
			pmove.append(cmove[p-1][q])
		if (p-1 in range(8)) and (q in range(8)):
			if piece[0]=='W':
				if board[p-1][q][0]=='B':
					pmove.append(cmove[p-1][q])
			else:
				if board[p-1][q][0]=='W':
					pmove.append(cmove[p-1][q])
		if (p-1 in range(8)) and (q-1 in range(8)) and ((board[p-1][q-1]=="///") or (board[p-1][q-1]=="   ")):
			pmove.append(cmove[p-1][q-1])
		if (p-1 in range(8)) and (q-1 in range(8)):
			if piece[0]=='W':
				if board[p-1][q-1][0]=='B':
					pmove.append(cmove[p-1][q-1])
			else:
				if board[p-1][q-1][0]=='W':
					pmove.append(cmove[p-1][q-1])
		if (p in range(8)) and (q-1 in range(8)) and ((board[p][q-1]=="///") or (board[p][q-1]=="   ")):
			pmove.append(cmove[p][q-1])
		if (p in range(8)) and (q-1 in range(8)):
			if piece[0]=='W':
				if board[p][q-1][0]=='B':
					pmove.append(cmove[p][q-1])
			else:
				if board[p][q-1][0]=='W':
					pmove.append(cmove[p][q-1])
		if (p+1 in range(8)) and (q-1 in range(8)) and ((board[p+1][q-1]=="///") or (board[p+1][q-1]=="   ")):
			pmove.append(cmove[p+1][q-1])
		if (p+1 in range(8)) and (q-1 in range(8)):
			if piece[0]=='W':
				if board[p+1][q-1][0]=='B':
					pmove.append(cmove[p+1][q-1])
			else:
				if board[p+1][q-1][0]=='W':
					pmove.append(cmove[p+1][q-1])
		if piece[0]=='W':
			if (x=='E1') and (kwmove=="") and (board[7][5]=="///") and (board[7][6]=="   ") and (board[7][7]=="WR2"):
				pmove.append('G1')
			if (x=='E1') and (kwmove=="") and (board[7][3]=="///") and (board[7][2]=="   ") and (board[7][1]=='///') and (board[7][0]=="WR1"):
				pmove.append('B1')
		if piece[0]=='B':
			if (x=='E8') and (kbmove=="") and (board[0][5]=="   ") and (board[0][6]=="///") and (board[0][7]=="BR2"):
				pmove.append('G8')
			if (x=='E8') and (kbmove=="") and (board[0][3]=="   ") and (board[0][2]=="///") and (board[0][1]=='   ') and (board[0][0]=="BR1"):

				pmove.append('B8')
		pmove=kingmove(piece,pmove,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb)
	return pmove
			
		
