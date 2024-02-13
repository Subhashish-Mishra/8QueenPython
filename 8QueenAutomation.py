# 8  Queen Automation

import turtle
#import EightQPshapes as es
import EightQueenproblem as eq
import random as ran
import RemoveDuplicate as rd

t = turtle.Turtle()
s = turtle.Screen()

SCALE = eq.SCALE
TilesPos = []
Quick = False

def CheckCross(r,c):
	#print('Checking SideWise....')
	for i in range(eq.BS):
		if (r,i) in TilesPos:
			return True
		if (i,c) in TilesPos:
			return True
	return False
def CheckDiag(R,C):
	#print('Checking Diagonal....')
	r,c = R,C
	while 0 <= r <= 7 and 0 <= c <= 7:
		if (r,c) in TilesPos:
			return True
		r,c = r+1,c-1
	r,c = R,C	
	while 0 <= r <= 7 and 0 <= c <= 7:
		if (r,c) in TilesPos:
			return True
		r,c = r-1,c+1
	r,c = R,C	
	while 0 <= r <= 7 and 0 <= c <= 7:
		if (r,c) in TilesPos:
			return True
		r,c = r+1,c+1
	r,c = R,C	
	while 0 <= r <= 7 and 0 <= c <= 7:
		if (r,c) in TilesPos:
			return True
		r,c = r-1,c-1
	return False

def Restart():
	t.clear()
	TilesPos.clear()
	#eq.drawBoard(8)
	eq.Counter = 1
	t.pencolor('red')
	r,c = ran.randint(0,7),ran.randint(0,7)
	print(r,',',c,end='')
	if Quick:
		t.up()
		t.goto(-4*SCALE+c*SCALE+SCALE/2-5,4*SCALE-r*SCALE-SCALE/2-8) # c , r
		t.down()
		t.write('q'+str(eq.Counter),font=('Consolas',16,'bold'))
	eq.Counter += 1
	TilesPos.append((r,c))

	for i in range(7,-1,-1):
		for j in range(7,-1,-1):
			if Quick:
				t.up()
				t.goto(-4*SCALE+j*SCALE+SCALE/2-5,4*SCALE-i*SCALE-SCALE/2-8) # c , r
				t.down()
			if CheckDiag(i,j) or CheckCross(i,j):
				pass
			else:
				if Quick:
					t.write('q'+str(eq.Counter),font=('Consolas',16,'bold'))
				eq.Counter += 1
				TilesPos.append((i,j))
	print(TilesPos,' ',len(TilesPos))
	if eq.Counter == 9:
		f = open('EQSolutions.txt','a')
		# f.write('\n')
		f.write(str(TilesPos))
		f.write('\n')
		f.close()
	else:
		Restart()

Restart()	
s.onkeypress(Restart,'r')
s.listen
s.mainloop()
rd.RemoveDuplicate()