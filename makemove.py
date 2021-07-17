def makemove(piece,move,board,awpiece,abpiece,kwmove,kbmove,cmove,prw,prb,stop=1):
	import copy 
	if piece[0]=='W':
		if (kwmove=="") and ((move=='G1') or (move=='B1')):
			if move=='G1':
				awpiece[12][1]='G1'
				awpiece[15][1]='F1'
				board[7][4]='   '
				board[7][5]='WR2'
				board[7][6]='W K'
				board[7][7]='///'
			else:
				awpiece[12][1]='B1'
				awpiece[8][1]='C1'
				board[7][0]='   '
				board[7][2]='WR1'
				board[7][1]='W K'
				board[7][4]='   '
		else:
			for l in range(16):
				if piece==awpiece[l][0]:
					a=awpiece[l][1]				
					awpiece[l][1]=move
					for i in range(8):
						for j in range(8):
							if cmove[i][j]==move:
								if board[i][j][0]=="B":
									for k in range(16):
										if board[i][j]==abpiece[k][0]:
											abpiece[k][1]="  "
											abpiece[k][0]='   ' 			
								board[i][j]=piece
					for i in range(8):
						for j in range(8):
							if cmove[i][j]==a:
								if (i+j)%2==0:							
									board[i][j]='///'
								else:
									board[i][j]='   '
			if (piece[1]=='P') and (move[1]=='8') and (stop==0):
				print ("PROMOTION OF PAWN")
				k='yes'
				prw+=1
				while k=='yes':
					print ("Specify the rank (B-Bishop,R-Rook,K-Knight,Q-Queen):")			
					pi=input()
					if pi not in ['B','R','K','Q']:
						print("Wrong rank press any letter to choose correct rank:")						
						l=input()
						k='yes'
					else:
						k='no'		
				for i in range(8):
					if piece==awpiece[i][0]:
						pi="W"+pi+str(prb+2)
						pl=awpiece[i][1]
						el=[]
						el.append(pi)
						el.append(pl)
						awpiece[i]=el	
						for j in range(8):
							if board[0][j]==piece:
								board[0][j]=pi	
	else:
		if (kbmove=="") and ((move=='G8') or (move=='B8')):
			if move=='G8':
				abpiece[12][1]='G8'
				abpiece[15][1]='F8'
				board[0][4]='///'
				board[0][5]='BR2'
				board[0][6]='B K'
				board[0][7]='   '
			else:
				abpiece[12][1]='B8'
				abpiece[8][1]='C8'
				board[0][0]='///'
				board[0][2]='BR1'
				board[0][1]='B K'
				board[0][4]='///'
		else:
			for l in range(16):
				if piece==abpiece[l][0]:
					a=abpiece[l][1]				
					abpiece[l][1]=move
					for i in range(8):
						for j in range(8):
							if cmove[i][j]==move:
								if board[i][j][0]=="W":
									for k in range(16):
										if board[i][j]==awpiece[k][0]:
											awpiece[k][1]="  "
											awpiece[k][0]="   "
								board[i][j]=piece
					for i in range(8):
						for j in range(8):
							if cmove[i][j]==a:
								if (i+j)%2==0:							
									board[i][j]='///'
								else:
									board[i][j]='   '
			if (piece[1]=='P') and (move[1]=='1') and (stop==0):
				print ("PROMOTION OF PAWN")
				k='yes'
				prb+=1
				while k=='yes':
					print ("Specify the rank (B-Bishop,R-Rook,K-Knight,Q-Queen):")
					pi=input()
					if pi not in ['B','R','K','Q']:
						print("Wrong rank press any letter to choose correct rank:")						
						l=input()
						k='yes'
					else:
						k='no'		
				for i in range(8):
					if piece==awpiece[i][0]:
						pi="W"+pi+str(prb+2)
						pl=awpiece[i][1]
						el=[]
						el.append(pi)
						el.append(pl)
						awpiece[i]=el				
						for j in range(8):
							if board[0][j]==piece:
								board[0][j]=pi
	wpiece=copy.deepcopy(awpiece)
	bpiece=copy.deepcopy(abpiece)						
	return (board)	
