# 8 Queen problem

import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
#t.speed(0)
t.ht()

#-----Global Variables-----
ScreenSize = turtle.screensize()
print(ScreenSize)
BS=8
SCALE = 760/BS-(20)
print(SCALE,',',BS)
col=['black','white']
Counter = 1
Limited = False
TilesPos = []
s.listen()
def GotoXY(x,y):
	t.up()
	t.goto(x,y)
	t.down()
def Square():
	for i in range(4):
		t.fd(SCALE)
		t.lt(90)
def drawBoard(n):
	t.speed(0)	
	c=0
	t.up()
	t.home()
	t.clear()
	t.goto(-(BS/2-1)*SCALE,-(BS/2)*SCALE)
	t.lt(90)
	t.down()
	for i in range(n):
		for j in range(n):
			t.begin_fill()
			t.color('red',col[c%2])
			c += 1
			Square()
			if j<n-1 and i%2==0:
				t.up()
				t.rt(90)
				t.fd(SCALE)
				t.lt(90)
				t.down()
			elif j<n-1:
				t.up()
				t.lt(90)
				t.fd(SCALE)
				t.rt(90)
				t.down()
			t.end_fill()
		t.up()
		t.fd(SCALE)
		t.down()
def RowColumn(x,y):
	r = -(y//SCALE-3.0)
	c = x//SCALE+4.0
	return int(r),int(c)
def CheckTile(x,y):
	r,c = RowColumn(x,y)
	if 0 <= r <= 7 and 0 <= c <= 7:
		return True
	return False
def gotoTile(x,y):
	if CheckTile(x,y):
		r,c = RowColumn(x,y)
		t.up()
		t.goto(-4*SCALE+c*SCALE+SCALE/2-5,4*SCALE-r*SCALE-SCALE/2-8)
		t.down()
def writeT(x,y):
	global Counter
	r,c = RowColumn(x,y)
	if CheckTile(x,y) and (r,c) not in TilesPos:
		t.pencolor('green')
		if CheckCross(x,y) or CheckDiag(x,y):
			print("\tFound in either Cross or Diagonal")
			t.pencolor('red')
		print('writeTile\t',end='')
		t.up()
		print(str(x)+','+str(y)+'\t',end='')
		print(str(r)+','+str(c))
		gotoTile(x,y)
		t.write('q'+str(Counter),font=('Consolas',16,'bold'))
		t.down()
		Counter += 1
		TilesPos.append((r,c))
def writeTile(x,y):
	if CheckTile(x,y):
		if Limited:
			if Counter<9:
				writeT(x,y)
		else:
			writeT(x,y)
def clearTile(x,y):
	global Counter
	r,c = RowColumn(x,y)
	if CheckTile(x,y) and (r,c) in TilesPos:
		print('clearTile\t',end='')
		print(str(x)+','+str(y)+'\t',end='')
		print(str(r)+','+str(c))
		t.up()
		t.goto(-4*SCALE+(c+1)*SCALE,4*SCALE-(r+1)*SCALE)
		t.down()
		t.begin_fill()
		t.color('red',col[int(r+c+1)%2])
		Square()
		t.end_fill()
		TilesPos.remove((r,c))
		Counter -= 1
	else:
		print("Empty Tile")

def CheckCross(x,y):
	print('Checking SideWise....')
	r,c = RowColumn(x,y)
	for i in range(BS):
		if (r,i) in TilesPos:
			return True
		if (i,c) in TilesPos:
			return True
	return False

def CheckDiag(x,y):
	print('Checking Diagonal....')
	r,c = RowColumn(x,y)
	while 0 <= r <= 7 and 0 <= c <= 7:
		if (r,c) in TilesPos:
			return True
		r,c = r+1,c-1
	r,c = RowColumn(x,y)
	while 0 <= r <= 7 and 0 <= c <= 7:
		if (r,c) in TilesPos:
			return True
		r,c = r-1,c+1
	r,c = RowColumn(x,y)
	while 0 <= r <= 7 and 0 <= c <= 7:
		if (r,c) in TilesPos:
			return True
		r,c = r+1,c+1
	r,c = RowColumn(x,y)
	while 0 <= r <= 7 and 0 <= c <= 7:
		if (r,c) in TilesPos:
			return True
		r,c = r-1,c-1
	
	return False

def TPPrint():
	print(TilesPos,end='')
	print(len(TilesPos))
def ResetCounter():
	global Counter
	Counter = 1
	print("-----Counter is Reset")
def Restart():
	print("-----Restarting")
	global TilesPos
	TilesPos.clear()
	ResetCounter()
	#drawBoard(BS)
	Menu()
def LimitAlter():
	global Limited
	GotoXY(-600,0)
	t.pencolor('black')
	t.write("Counter limit is: "+str(Limited),font=('Consolas',12,'bold'))
	if Limited:
		Limited = False
	else:
		Limited = True
	t.pencolor('white')
	t.write("Counter limit is: "+str(Limited),font=('Consolas',12,'normal'))
	print("-----Counter limit is",Limited)
def KeyBindings():
	s.onclick(writeTile)
	s.onclick(clearTile,btn=3)
	s.onkeypress(TPPrint,'a')
	s.onkeypress(ResetCounter,'c')
	s.onkeypress(LimitAlter,'e')
	s.onkeypress(Restart,'r')
	s.listen()
def pxy(x,y):
	print(str(x),',',str(y))
#-----Game Code-----
def Button(x,y,S: str,size: int):
	GotoXY(x,y)
	t.write(S,align='center',move=True,font=('Consolas',size,'bold'))
def ButtonRed(x,y,S: str,size: int):
	t.pencolor('red')
	GotoXY(x,y)
	t.write(S,align='center',move=True,font=('Consolas',size,'bold'))
def Play(x,y):
	if -15 < x <15 and 20 < y < 35:
		ButtonRed(0,20,'Play',12)
		GameStart()
	if -17 < x < 17 and -10 < y < 5:
		ButtonRed(0,-10,'Quit',12)
		quit()
def Menu():
	t.speed(1)
	t.clear()
	t.pencolor('white')
	Button(0,50,"-------Menu-------",16)
	Button(0,20,'Play',12)
	Button(0,-10,'Quit',12)
	s.onclick(Play)
def GameStart():
	drawBoard(BS)
	KeyBindings()
#-----Driver Code-----
if __name__ == '__main__':
	#drawBoard(BS)
	Menu()
	#s.onclick(pxy)
	s.mainloop()

	#time.sleep(5)
	#78.778752