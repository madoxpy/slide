from pygame import *
from random import randint
from time import sleep

init()
res=[600,600]
window=display.set_mode(res)
clock=time.Clock()
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
yellow=(255,255,0)
lightred=(204,0,0)
lightblue=(51,153,255)
lightgreen=(153,255,51)
lightyellow=(255,255,102)
white=(255,255,255)
Font=font.SysFont("arial",20)

class Game(object):
	def __init__(self):
		self.tab=[[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,0]]
		for i in range(1000):
			r=randint(0,3)
			if r==0:
				self.down()
			elif r==1:
				self.up()
			elif r==2:
				self.left()
			else:
				self.right()
	def draw(self):
		window.fill(black)
		for j in range(4):
			for i in range(4):
				if self.tab[i][j]!=0:
					draw.rect(window,green,Rect(i*150,j*150,149,149),0)
					text = Font.render(str(self.tab[i][j]),True,white)
					window.blit(text,(i*150+70,j*150+70))
	def findzero(self):
		for i in range(4):
			for j in range(4):
				if self.tab[i][j]==0:
					return (i,j)
	def down(self):
		zero=self.findzero()
		if zero[1]>0:
			self.tab[zero[0]][zero[1]]=self.tab[zero[0]][zero[1]-1]
			self.tab[zero[0]][zero[1]-1]=0
	def up(self):
		zero=self.findzero()
		if zero[1]<3:
			self.tab[zero[0]][zero[1]]=self.tab[zero[0]][zero[1]+1]
			self.tab[zero[0]][zero[1]+1]=0		
	def left(self):
		zero=self.findzero()
		if zero[0]<3:
			self.tab[zero[0]][zero[1]]=self.tab[zero[0]+1][zero[1]]
			self.tab[zero[0]+1][zero[1]]=0
	def right(self):
		zero=self.findzero()
		if zero[0]>0:
			self.tab[zero[0]][zero[1]]=self.tab[zero[0]-1][zero[1]]
			self.tab[zero[0]-1][zero[1]]=0
game=Game()
end=False
while not end:
	game.draw()
	for z in event.get():
		if z.type==QUIT:
			end=True
		if z.type==KEYDOWN:
			if z.key== K_UP:
				game.up()
			if z.key== K_DOWN:
				game.down()
			if z.key== K_LEFT:
				game.left()
			if z.key== K_RIGHT:
				game.right()
	

	display.flip()
	clock.tick(20)
