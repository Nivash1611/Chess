def checkpiece(player,piece,wpiece,bpiece):
	if player==1:
		for i in range(16):
			if piece==wpiece[i][0]:
				return "yes"
		return "no"
	if player==2:
		for i in range(16):
			if piece==bpiece[i][0]:
				return "yes"
		return "no"





		
