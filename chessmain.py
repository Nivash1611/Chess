global wpiece
global bpiece
global cmove
global prb
global prw
global kwmove
global kbmove
wpiece=[['WP1','A2'],['WP2','B2'],['WP3','C2'],['WP4','D2'],['WP5','E2'],['WP6','F2'],['WP7','G2'],['WP8','H2'],['WR1','A1'],['WK1','B1'],['WB1','C1'],['WQ1','D1'],['W K','E1'],['WB2','F1'],['WK2','G1'],['WR2','H1']]
bpiece=[['BP1','A7'],['BP2','B7'],['BP3','C7'],['BP4','D7'],['BP5','E7'],['BP6','F7'],['BP7','G7'],['BP8','H7'],['BR1','A8'],['BK1','B8'],['BB1','C8'],['BQ1','D8'],['B K','E8'],['BB2','F8'],['BK2','G8'],['BR2','H8']]
pmove=[]
board=[['BR1','BK1','BB1','BQ1','B K','BB2','BK2','BR2'],['BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8'],['///','   ','///','   ','///','   ','///','   '],['   ','///','   ','///','   ','///','   ','///'],['///','   ','///','   ','///','   ','///','   '],['   ','///','   ','///','   ','///','   ','///'],['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8'],['WR1','WK1','WB1','WQ1','W K','WB2','WK2','WR2']]
cmove=[['A8','B8','C8','D8','E8','F8','G8','H8'],['A7','B7','C7','D7','E7','F7','G7','H7'],['A6','B6','C6','D6','E6','F6','G6','H6'],['A5','B5','C5','D5','E5','F5','G5','H5'],['A4','B4','C4','D4','E4','F4','G4','H4'],['A3','B3','C3','D3','E3','F3','G3','H3'],['A2','B2','C2','D2','E2','F2','G2','H2'],['A1','B1','C1','D1','E1','F1','G1','H1']]
prb=1
prw=1
kwmove=""
kbmove=""
player=1
from draw import *
from blockcheck import * 
from check import *
from checkmate import *
from checkpiece import *
from chessboard import *
from kingmove import *
from makemove import *
from opencheck import *
from possiblemove import *
from os import system
print (" WELCOME TO WIZARD CHESS ")
print (" If you want to accept your defeat type DEF while choosing piece")
print (" Player 1 = White, Player 2 = Black")
print (" Enter any Key to start the War ")
abcd=input()
state="BAT"
i=0
piece="   "
cpiece=[]
kpmove=[]
lpiece=piece
while state=="BAT":
	chessboard(board)
	i+=1
	if i%2==0:
		player=2
	else:
		player=1
	print("Player :",player)
	poss=0
	while poss==0:
		res="no"
		while res=="no":
			print("Choose a piece to move:")
			piece=input()
			if piece=="DEF":
				print("Player ",player," lose the game")
				print("press any key to quit the game")
				pqr=input()
				exit()
			res=checkpiece(player,piece,wpiece,bpiece)
			if res=="no":
				print("Sorry!!! Invalid piece")
		if lpiece not in ["   "]:
			cpiece=check(lpiece,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb)
		Z1=0
		for j1 in cpiece:
			Z1+=1
		if Z1==0:
			if player==1:
				kpmove=possiblemove('W K',board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
			else:
				kpmove=possiblemove('B K',board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
			Z2=0
			for j2 in kpmove:
				Z2+=1
			if Z2==0:
				draw(lpiece,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
			pmove=possiblemove(piece,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
			if piece not in ['W K','B K']:
				pmove=opencheck(pmove,piece,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb)
		else:
			print("CHECK!!!")
			if player==1:
				kpmove=possiblemove('W K',board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
			else:
				kpmove=possiblemove('B K',board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
			Z3=0
			for j3 in kpmove:
				Z3+=1
			if Z3==0:
				checkmate(lpiece,board,wpiece,bpiece,prw,prb,cpiece,cmove,kwmove,kbmove)
			if piece[2]=="K":
				pmove=possiblemove(piece,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
			else:
				pmove=possiblemove(piece,board,wpiece,bpiece,cmove,kwmove,kbmove,prw,prb)
				Z=0
				for j in cpiece:
					Z+=1				
				if Z==1:
					pmove=blockcheck(cpiece,piece,pmove,board,wpiece,bpiece,cmove)
				else:
					pmove=[]
				pmove=opencheck(pmove,piece,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb)
		if pmove==[]:
			poss=0
			print("Sorry!!! No Possible Move for given piece")
		else:
			poss=1
	pmo=0
	while pmo==0:
		print("Possible Moves For Selected Piece:")
		print(pmove)
		print("Choose any place from possible moves:")
		move=input()
		if move not in pmove:
			pmo=0
			print("Sorry Wrong Place")
		else:
			pmo=1
	if piece[0]=='W':
		for I in range(16):
			if piece==wpiece[I][0]:
				plaze=I
	if piece[0]=='B':
		for I in range(16):
			if piece==bpiece[I][0]:
				plaze=I
	board=makemove(piece,move,board,wpiece,bpiece,kwmove,kbmove,cmove,prw,prb,0)
	if piece[0]=='W':
		lpiece=wpiece[plaze][0]
	if piece[0]=='B':
		lpiece=bpiece[plaze][0]
	print(lpiece)
	if piece=='W K':
		kwmove="m"
	if piece=='B K':
		kbmove='m'
	
	
	
		
		
		
			
		
		
	

	 
