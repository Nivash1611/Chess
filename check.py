def check(piece,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb):
	from possiblemove import possiblemove
	cpiece=[]
	pmove=possiblemove(piece,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
	if piece[0]=='B':
		x=wpiece[12][1]
		for i in range(8):
			for j in range(8):
				if x==cmove[i][j]:
					p=i
					q=j
		if (piece[1]=='K') or (piece[1]=='P'):
			for i in pmove:
				if i==wpiece[12][1]:
					cpiece.append(piece)
	else:
		x=bpiece[12][1]
		for i in range(8):
			for j in range(8):
				if x==cmove[i][j]:
					p=i
					q=j
		if (piece[1]=='K') or (piece[1]=='P'):
			for i in pmove:
				if i==bpiece[12][1]:
					cpiece.append(piece)
	a=p+1
	b=q+1	
	while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
		a+=1
		b+=1
	if (a in range(8)) and (b in range(8)):
		if piece[0]=='B':
			if board[a][b][0]=='B':
				if (board[a][b][1]=='B') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
		else:
			if board[a][b][0]=='W':
				if (board[a][b][1]=='B') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
	a=p+1
	b=q-1
	while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
		a+=1
		b-=1
	if (a in range(8)) and (b in range(8)):
		if piece[0]=='B':
			if board[a][b][0]=='B':
				if (board[a][b][1]=='B') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
		else:
			if board[a][b][0]=='W':
				if (board[a][b][1]=='B') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
	a=p-1
	b=q-1
	while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
		a-=1
		b-=1
	if (a in range(8)) and (b in range(8)):
		if piece[0]=='B':
			if board[a][b][0]=='B':
				if (board[a][b][1]=='B') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
		else:
			if board[a][b][0]=='W':
				if (board[a][b][1]=='B') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
	a=p-1
	b=q+1
	while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
		a-=1
		b+=1
	if (a in range(8)) and (b in range(8)):
		if piece[0]=='B':
			if board[a][b][0]=='B':
				if (board[a][b][1]=='B') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
		else:
			if board[a][b][0]=='W':
				if (board[a][b][1]=='B') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
	a=p+1
	b=q	
	while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
		a+=1
	if (a in range(8)) and (b in range(8)):
		if piece[0]=='B':
			if board[a][b][0]=='B':
				if (board[a][b][1]=='R') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
		else:
			if board[a][b][0]=='W':
				if (board[a][b][1]=='R') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
	a=p-1
	b=q
	while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
		a-=1
	if (a in range(8)) and (b in range(8)):
		if piece[0]=='B':
			if board[a][b][0]=='B':
				if (board[a][b][1]=='R') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
		else:
			if board[a][b][0]=='W':
				if (board[a][b][1]=='R') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
	a=p
	b=q+1
	while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
		b+=1
	if (a in range(8)) and (b in range(8)):
		if piece[0]=='B':
			if board[a][b][0]=='B':
				if (board[a][b][1]=='R') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
		else:
			if board[a][b][0]=='W':
				if (board[a][b][1]=='R') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
	a=p
	b=q-1
	while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
		b-=1
	if (a in range(8)) and (b in range(8)):
		if piece[0]=='B':
			if board[a][b][0]=='B':
				if (board[a][b][1]=='R') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
		else:
			if board[a][b][0]=='W':
				if (board[a][b][1]=='R') or (board[a][b][1]=='Q'):
					cpiece.append(board[a][b])
	return cpiece



	
				
