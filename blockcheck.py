def blockcheck(cpiece,piece,pmove,board,wpiece,bpiece,cmove):
	bmove=[]	
	xmove=[]
	import copy
	if cpiece[0][1]=='B':
		if piece[0]=='W':
			x=wpiece[12][1]
		else:
			x=bpiece[12][1]
		for i in range(8):
			for j in range(8):
				if cmove[i][j]==x:
					p=i
					q=j
		a=p
		b=q	
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a+=1
			b+=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):			
				if board[a][b][1]=='B':
					bmove=copy.deepcopy(xmove)
		xmove=[]		
		a=p
		b=q
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a+=1
			b-=1
			xmove.append(cmove[a][b])		
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='B':
					bmove=copy.deepcopy(xmove)
		xmove=[]		
		a=p
		b=q
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a-=1
			b-=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='B':
					bmove=copy.deepcopy(xmove)
		xmove=[]		
		a=p
		b=q
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a-=1
			b+=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='B':
					bmove=copy.deepcopy(xmove)
	if cpiece[0][1]=='R':
		if piece[0]=='W':
			x=wpiece[12][1]
		else:
			x=bpiece[12][1]
		for i in range(8):
			for j in range(8):
				if cmove[i][j]==x:
					p=i
					q=j
		a=p
		b=q	
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a+=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='R':
					bmove=copy.deepcopy(xmove)
		a=p
		b=q
		xmove=[]
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a-=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='R':
					bmove=copy.deepcopy(xmove)
		a=p
		b=q
		xmove=[]
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			b+=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='R':
					bmove=copy.deepcopy(xmove)
		a=p
		b=q
		xmove=[]
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			b-=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='R':
					bmove=copy.deepcopy(xmove)
	if cpiece[0][1]=='Q':
		if piece[0]=='W':
			x=wpiece[12][1]
		else:
			x=bpiece[12][1]
		for i in range(8):
			for j in range(8):
				if cmove[i][j]==x:
					p=i
					q=j
		a=p
		b=q	
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a+=1
			b+=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):			
				if board[a][b][1]=='Q':
					bmove=copy.deepcopy(xmove)
		xmove=[]		
		a=p
		b=q
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a+=1
			b-=1
			xmove.append(cmove[a][b])		
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='Q':
					bmove=copy.deepcopy(xmove)
		xmove=[]		
		a=p
		b=q
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a-=1
			b-=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='Q':
					bmove=copy.deepcopy(xmove)
		xmove=[]		
		a=p
		b=q
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a-=1
			b+=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='Q':
					bmove=copy.deepcopy(xmove)
		xmove=[]
		a=p
		b=q	
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a+=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='Q':
					bmove=copy.deepcopy(xmove)
		a=p
		b=q
		xmove=[]
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			a-=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='Q':
					bmove=copy.deepcopy(xmove)
		a=p
		b=q
		xmove=[]
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			b+=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='Q':
					bmove=copy.deepcopy(xmove)
		a=p
		b=q
		xmove=[]
		while (a in range(8)) and (b in range(8)) and ((board[a][b]=="///") or (board[a][b]=="   ")):
			b-=1
			xmove.append(cmove[a][b])
		if (a in range(8)) and (b in range(8)):
			if (((piece[0]=='W') and (board[a][b][0]=='B')) or ((piece[0]=='B') and (board[a][b][0]=='W'))):
				if board[a][b][1]=='Q':
					bmove=copy.deepcopy(xmove)
	if cpiece[0][1]=='K':
		if piece[0]=='B':
			if cpiece[0]==wpiece[9][0]:
				x=wpiece[9][1]
			elif cpiece[0]==wpiece[14][1]:
				x=wpiece[14][1]
			else:
				for d in range(8):
					if piece==wpiece[d][0]:
						x=wpiece[d][1]
		if piece[0]=='W':
			if cpiece[0]==bpiece[9][0]:
				x=bpiece[9][1]
			elif cpiece[0]==bpiece[14][1]:
				x=bpiece[14][1]
			else:
				for d in range(8):
					if piece==bpiece[d][0]:
						x=bpiece[d][1]
		bmove.append(x)	
	if cpiece[0][1]=='P':
		if piece[0]=='B':
			for i in range(8):
				if cpiece[0]==wpiece[i][0]:
					x=wpiece[i][1]
		if piece[0]=='W':
			for i in range(8):
				if cpiece[0]==bpiece[i][0]:
					x=bpiece[i][1]
		bmove.append(x)
	zmove=[]
	for i in pmove:
		if i in bmove:
			zmove.append(i)
	pmove=[]
	pmove=copy.deepcopy(zmove)
	return pmove
			

			
