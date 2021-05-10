import pygame
pygame.init()

win=pygame.display.set_mode((720,1370))

"""
1-simple brick
2=double brick
3=triple brick
4=quad brick
s=score+1000
b=extra ball
l=extra life
"""
#colors
bg=(200,200,200)
bound1=(100,150,250)
bound2=(250,250,200)
paddle_col=(100,100,100)
brick1=(0,0,0)
brick2=(100,0,0)
brick3=(100,100,0)
brick4=(0,100,100)


run=1
clock=pygame.time.Clock()
fps=10

def boundary():
	for i in range(70,1370,200):
		pygame.draw.rect(win,bound1,[0,i,40,100])
		pygame.draw.rect(win,bound2,[0,i+100,40,100])
		pygame.draw.rect(win,bound1,[680,i,40,100])
		pygame.draw.rect(win,bound2,[680,i+100,40,100])
	for i in range(20,720,200):
		pygame.draw.rect(win,bound1,[i,70,100,40])
		pygame.draw.rect(win,bound2,[i+100,70,100,40])
		pygame.draw.rect(win,bound1,[i,1330,100,40])
		pygame.draw.rect(win,bound2,[i+100,1330,100,40])
		
class paddle():
	def __init__(self):
		self.paddle_x=360
		self.paddle_y=1152
		self.direction=0
		self.speed=10
		self.rect=pygame.Rect([self.paddle_x-100,self.paddle_y,200,50])
	
	def move(self):
		for ev in pygame.event.get():
			if ev.type==pygame.MOUSEMOTION:
				pos=pygame.mouse.get_pos()	
				if pos[0]>140 and pos[0]<580:
					self.rect.right=pos[0]+100
				
	def draw(self):
		pygame.draw.rect(win,paddle_col,self.rect)
		pygame.draw.rect(win,"black",self.rect,5)

class drawer():
	def __init__(self):
		self.x=54
		self.y=117
		self.vel_x=128
		self.vel_y=71
		self.bricks=[]
		self.special=None
		
	def move(self):
		key=pygame.key.get_pressed()
		if key[pygame.K_UP] and self.y>117:
			self.y-=self.vel_y
		elif key[pygame.K_DOWN] and self.y<1000:
			self.y+=self.vel_y
		elif key[pygame.K_RIGHT] and self.x<560:
			self.x+=self.vel_x
		elif key[pygame.K_LEFT] and self.x>54:
			self.x-=self.vel_x
			
	def draw(self):
		self.rect=pygame.Rect([self.x,self.y,100,50])		
		pygame.draw.rect(win,"red",self.rect)
		key=pygame.key.get_pressed()
		if key[pygame.K_1]:
			rec=[self.x,self.y,100,50]
			brick=[rec,1,self.special]
			if brick not in self.bricks:
				self.bricks.append(brick)
				print(self.bricks)
							
		elif key[pygame.K_2]:
			rec=[self.x,self.y,100,50]
			brick=[rec,2,self.special]
			if brick not in self.bricks:
				self.bricks.append(brick)
		elif key[pygame.K_3]:
			rec=[self.x,self.y,100,50]
			brick=[rec,3,self.special]
			if brick not in self.bricks:
				self.bricks.append(brick)
		elif key[pygame.K_4]:
			rec=[self.x,self.y,100,50]
			brick=[rec,4,self.special]
			if brick not in self.bricks:
				self.bricks.append(brick)
		elif key[pygame.K_b]:
			self.special="fireball"
		elif key[pygame.K_l]:
			self.special="life"
		elif key[pygame.K_s]:
			 self.special="s+100"
		elif key[pygame.K_RETURN]:
			with open("level.txt","a") as f:
				if self.bricks!=[]:
					level=str(self.bricks)+"\n"
					f.write(level)
			quit()
			
			
		for i in self.bricks:
			if i[1]==1:
				color=brick1
			elif i[1]==2:
				color=brick2
			elif i[1]==3:
				color=brick3
			else:
				color=brick4
			pygame.draw.rect(win,color,i[0])

pad=paddle()		
drawer=drawer()
												
while run:
	win.fill(bg)
	pad.draw()
	pad.move()
	drawer.move()
	drawer.draw()
	boundary()
	pygame.display.update()
	clock.tick(fps)