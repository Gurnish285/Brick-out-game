import pygame
pygame.init()
pygame.mixer.init()
win=pygame.display.set_mode((720,1370))

#colors
bg=(200,200,200)
bound1=(46,139,87)
bound2=(189,183,107)
paddle_col=(100,100,100)
brick1=(0,128,0)
brick2=(112,118,144)
brick3=(153,50,10)
brick4=(0,0,100)
ball_col=(100,200,200)
font1_col=(87,107,47)
font2_col=(200,200,200)
mbox_col=(0,0,250)
mbox2_col=(0,200,0)

run=1
start=0
gameover=0
clock=pygame.time.Clock()
fps=60
level=1
life=3
instruction=1
menu=0
score=0
level_over=0
difficulty=1
level_list=[]

#managing level
with open("level_no.txt","a") as f:
	pass
with open("level_no.txt") as f:
	l=f.read()
	if l=="":
		level=1
	else:	
		level=int(l)
#_____________

#______________________
#reading file to create level
with open("level.txt") as f:
	text=f.readlines()

for i in text:
	level_=eval(i)
	level_list.append(level_)
	
#_____________________

#boundary drawing
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

#bricks on screen

def bricks():
	i=level_list[level-1]
	color=brick1
	for j in i:
		if j[1]==1:
			color=brick1
		elif j[1]==2:
			color=brick2
		elif j[1]==3:
			color=brick3	
		elif j[1]==4:
			color=brick4
		pygame.draw.rect(win,color,j[0])	

#_________text__________		
class text():
	def __init__(self):
		self.font1=pygame.font.SysFont("times new roman",40)
		self.font2=pygame.font.SysFont("hexatic",50)
		self.font3=pygame.font.SysFont("times new roman",20)
		self.vel_text=10
		self.fall_list=[]
		
	def top(self):
		level_text=self.font1.render("Level="+str(level),1,font1_col)
		life_text=self.font1.render("Life="+str(life),1,font1_col)		
		score_text=self.font1.render("Score="+str(score),1,font1_col)
		win.blit(level_text,(50,10))
		win.blit(life_text,(270,10))
		win.blit(score_text,(450,10))
	def menu(self):
		global difficulty,level,instructions,menu
		text1=self.font2.render("Difficulty",1,"brown")
		text2=self.font2.render("Level",1,"brown")
		text_dif=self.font2.render(str(difficulty),1,"blue")
		text_level=self.font2.render(str(level),1,"blue")
		
		pygame.draw.rect(win,mbox2_col,[180,490,350,240])
		pygame.draw.rect(win,"black",[175,485,360,250],10)
		pygame.draw.polygon(win,"red",[(200,530),(230,505),(230,555)])
		pygame.draw.polygon(win,"red",[(510,530),(480,505),(480,555)])
		pygame.draw.polygon(win,"red",[(200,650),(230,625),(230,675)])
		pygame.draw.polygon(win,"red",[(510,650),(480,625),(480,675)])
		win.blit(text1,(280,570))
		win.blit(text2,(310,680))
		win.blit(text_dif,(340,515))
		win.blit(text_level,(340,635))
		for ev in pygame.event.get():
			if ev.type==pygame.MOUSEMOTION:
				pos=pygame.mouse.get_pos()
				if pos[0]>=105 and pos[0]<=490 and pos[1]>=165 and pos[1]<=528 and start==0:
					menu=not menu
				
				elif pos[0]>=195 and pos[0]<=235 and pos[1]>=505 and pos[1]<=555 and difficulty>1:
					difficulty-=1
					if difficulty==1:
						gameball.vel_x=7
						gameball.vel_y=-7
						gameball.collision_no=8
					elif difficulty==2:
						gameball.vel_x=10
						gameball.vel_y=-10
						gameball.collision_no=11
					elif difficulty==3:
						gameball.vel_x=15
						gameball.vel_y=-15
						gameball.collision_no=16
					
				elif pos[0]>=195 and pos[0]<=235 and pos[1]>=625 and pos[1]<=675 and level>1:
					level-=1
					instructions=0
				elif pos[0]>=475 and pos[0]<=525 and pos[1]>=505 and pos[1]<=555 and difficulty<3:
					difficulty+=1
					if difficulty==1:
						gameball.vel_x=7
						gameball.vel_y=-7
						gameball.collision_no=8
					elif difficulty==2:
						gameball.vel_x=10
						gameball.vel_y=-10
						gameball.collision_no=11
					elif difficulty==3:
						gameball.vel_x=15
						gameball.vel_y=-15
						gameball.collision_no=16
				
				elif pos[0]>=475 and pos[0]<=525 and pos[1]>=625 and pos[1]<=675 and level<(len(level_list)):
					level+=1
	def start_message(self):
		message=self.font2.render("Click \"here\" to start",1,font2_col)
		pygame.draw.rect(win,mbox_col,[100,485,520,400])
		pygame.draw.rect(win,"black",[95,480,530,410],10)
		win.blit(message,(200,670))
		pygame.draw.rect(win,"white",[105,490,60,38],2)
		pygame.draw.rect(win,"white",[110,497,50,5])
		pygame.draw.rect(win,"white",[110,507,50,5])
		pygame.draw.rect(win,"white",[110,517,50,5])
		if menu==1:
			self.menu()
	
	def no_levels(self):
		message1=self.font2.render("Sorry, no more levels",1,font2_col)
		message2=self.font2.render("Ask GURNISH to add more",1,font2_col)
		pygame.draw.rect(win,mbox_col,[100,485,520,400])
		pygame.draw.rect(win,"black",[95,480,530,410],10)
		win.blit(message1,(180,620))
		win.blit(message2,(140,700))
		pygame.draw.rect(win,"white",[105,490,60,38],2)
		pygame.draw.rect(win,"white",[110,497,50,5])
		pygame.draw.rect(win,"white",[110,507,50,5])
		pygame.draw.rect(win,"white",[110,517,50,5])
		if menu==1:
			self.menu()
	
	def instructions(self):
		text1=self.font1.render("Instructions",1,"green")
		inst1=self.font2.render("- simple brick",1,font2_col)
		inst2=self.font2.render("- double power brick",1,font2_col)
		inst3=self.font2.render("- triple power brick",1,font2_col)
		inst4=self.font2.render("- hardest brick",1,font2_col)
		inst5=self.font3.render("(Click in centre of the screen to continue)",1,"red")
		pygame.draw.rect(win,mbox_col,[100,485,520,400])
		pygame.draw.rect(win,"black",[95,480,530,410],10)
		pygame.draw.rect(win,brick1,[120,580,100,50])
		pygame.draw.rect(win,brick2,[120,660,100,50])
		pygame.draw.rect(win,brick3,[120,740,100,50])
		pygame.draw.rect(win,brick4,[120,820,100,50])
		win.blit(text1,(230,500))
		win.blit(inst1,(270,585))
		win.blit(inst2,(270,665))
		win.blit(inst3,(270,745))
		win.blit(inst4,(270,825))
		win.blit(inst5,(170,545))
		
	def falling_text(self):
		global score,life
		for i in self.fall_list:
			text1=self.font2.render(i[1],1,"red")
			pos_=(i[0][0],i[0][1])
			win.blit(text1,(pos_))
			text_rect=pygame.Rect(i[0])
			text_y=pos_[1]
			if text_y>1300:
				self.fall_list.remove(i)
				
			elif text_rect.colliderect(pad.rect):
				if i[1]=="life":
					life+=1
				elif i[1]=="s+100":
					score+=1000
				elif i[1]=="fireball":
					gameball.fireball=1
				self.fall_list.remove(i)		
			else:	
				text_y+=self.vel_text
				i[0][1]=text_y
				
	def gameover(self):
		if gameover==-1:
			message1=self.font2.render("Game Over",1,"red")
			message2=self.font2.render("Click \"here\" to retry",1,font2_col)			
			pygame.draw.rect(win,mbox_col,[100,485,520,400])
			pygame.draw.rect(win,"black",[95,480,530,410],10)
		
			win.blit(message1,(270,650))
			win.blit(message2,(200,700))
		elif gameover==1:
			message1=self.font2.render("You Win",1,"green")
			message2=self.font2.render("Click \"here\" to move on",1,font2_col)			
			pygame.draw.rect(win,mbox_col,[100,485,520,400])
			pygame.draw.rect(win,"black",[95,480,530,410],10)
		
			win.blit(message1,(290,650))
			win.blit(message2,(170,700))
		
#__________________

#drawing paddle

class paddle():
	def __init__(self):
		self.paddle_x=360
		self.paddle_y=1152
		self.direction=0
		self.past_pos=[self.paddle_x]
		self.speed=10
		self.rect=pygame.Rect([self.paddle_x-100,self.paddle_y,200,50])
	
	def move(self):
		global start,gameover,instruction,menu
		for ev in pygame.event.get():
			if ev.type==pygame.MOUSEMOTION:
				pos=pygame.mouse.get_pos()
				if pos[0]>=105 and pos[0]<=490 and pos[1]>=165 and pos[1]<=528 and start==0:
					menu=not menu
				
				if pos[0]>=210 and pos[0]<510 and pos[1]>=635 and pos[1]<=935:
					if instruction==1:
						instruction=0
					else:
						start=1
					if gameover==-1:
						gameover=0
						start=0
						self.rect.left=360-100
						
						gameball.x=360
						gameball.y=1130
					elif gameover==1:
						gameover=0
						start=0
						self.rect.left=360-100
						gameball.x=360
						gameball.y=1130
						
				if pos!=[]:
					self.past_pos.append(pos[0]+100)
					self.past_pos.pop()
				if pos[0]>140 and pos[0]<580 and  pos[1]>900:
					self.rect.right=pos[0]+100
					if start==0:
						gameball.x=pos[0]
					if self.past_pos[0]<pos[0]:
						self.direction=1
					elif self.past_pos[0]>pos[0]:
						self.direction=-1
							
	def draw(self):
		pygame.draw.rect(win,paddle_col,self.rect)
		pygame.draw.rect(win,"black",self.rect,5)

#ball class

class ball():
	def __init__(self):
		self.radius=20
		self.x=360
		self.collision_no=7
		self.vel_x=5
		self.vel_y=-5
		self.y=1130	
		self.fireball=0	
	
	def draw(self):
		self.rect=pygame.Rect([self.x-self.radius,self.y-self.radius,40,40])
		pygame.draw.circle(win,ball_col,(self.x,self.y),self.radius)		

	def move(self):
		global gameover,start,life,level_list,level,score,level_over
		if start==1:
			#brick collsion
			cur_level=level_list[level-1]
			for i in range(len(cur_level)):
				if self.rect.colliderect(pygame.Rect(cur_level[i][0])):
					pygame.mixer.music.load("hit.mp3")
					pygame.mixer.music.play()
					score+=10
					if self.fireball==0:	
						# brick collision from below
						if abs(self.rect.top-pygame.Rect(cur_level[i][0]).bottom)<self.collision_no and self.vel_y<0:
							self.vel_y*=-1
							if cur_level[i][1]>1:
								cur_level[i][1]-=1
							elif cur_level[i][1]==1:
								game_text.fall_list.append([cur_level[i][0],cur_level[i][2]])
								level_list[level-1][i]=[[0,0,0,0],0,None]
						
						#brick collision from left side					
						elif abs(self.rect.left-pygame.Rect(cur_level[i][0]).right)<self.collision_no and self.vel_x<0:
						
							self.vel_x*=-1
							if cur_level[i][1]>1:
								cur_level[i][1]-=1
							elif cur_level[i][1]==1:
								game_text.fall_list.append([cur_level[i][0],cur_level[i][2]])
								level_list[level-1][i]=[[0,0,0,0],0,None]
						
						#brick collision from right side
						elif abs(self.rect.right-pygame.Rect(cur_level[i][0]).left)<self.collision_no and self.vel_x>0:
							self.vel_x*=-1
							if cur_level[i][1]>1:
								cur_level[i][1]-=1
							elif cur_level[i][1]==1:
								game_text.fall_list.append([cur_level[i][0],cur_level[i][2]])
								level_list[level-1][i]=[[0,0,0,0],0,None]
	
			#brick collision from above
						elif abs(self.rect.bottom-pygame.Rect(cur_level[i][0]).top)<self.collision_no and self.vel_y>0:
							self.vel_y*=-1
							if cur_level[i][1]>1:
								cur_level[i][1]-=1
							elif cur_level[i][1]==1:
								game_text.fall_list.append([cur_level[i][0],cur_level[i][2]])
								level_list[level-1][i]=[[0,0,0,0],0,None]

					elif self.fireball==1:
						level_list[level-1][i]=[[0,0,0,0],0,None]
						
			#boundary hit 
			if self.rect.right>=680 or self.rect.left<=40:
				self.vel_x*=-1
			if self.rect.top<=110:
				self.vel_y*=-1
				if self.fireball==1:
					self.fireball=0
			
			#brick damage checker
			count=0
			for i in cur_level:
				if i==[[0,0,0,0],0,None]:
					count+=1
			if count==len(cur_level):
				gameover=1
				self.fireball=0
				start=0
				life=3
				if level<len(level_list):
					level+=1
				else:
					level_over=1
					gameover=0
				#writing level number in file to save
				with open("level_no.txt","w") as f:
					f.write(str(level))
				
				#readig level
				with open("level.txt") as f:
					level_text=f.readlines()
				level_list=[]
				for i in level_text:
					level_=eval(i)
					level_list.append(level_)
						
			#gameover
			elif self.rect.bottom>1300:
				start=0
				pygame.mixer.music.load("gameover.mp3")
				pygame.mixer.music.play()
				gameover=-1
				life-=1
				self.fireball=0
				if life==0:
					with open("level.txt") as f:
						level_text=f.readlines()
					level_list=[]
					for i in level_text:
						level_=eval(i)
						level_list.append(level_)
					life=3
									
					#paddle top collision
			if self.rect.colliderect(pad.rect):
				if abs(self.rect.bottom-pad.rect.top)<self.collision_no and self.vel_y>0:
					self.vel_y*=-1			
				# paddle side collsion
				elif abs(self.rect.left-pad.rect.right)<self.collision_no and self.vel_x<0:
					self.vel_x*=-1
				elif abs(self.rect.right-pad.rect.left)>self.collision_no and self.vel_x>0:
					self.vel_x*=-1
			
			#velocity addition
			self.x+=self.vel_x
			self.y+=self.vel_y

#class instances
pad=paddle()		
game_text=text()
gameball=ball()
											
while run:
	win.fill(bg)
	bricks()
	game_text.top()
	
	if start==0:
		game_text.start_message()
	if gameover!=0:
		game_text.gameover()
	if level==1 and start==0 and instruction==1:
		game_text.instructions()
	pad.draw()
	pad.move()
	boundary()
	gameball.draw()
	gameball.move()
	if game_text.fall_list!=[]:
		game_text.falling_text()
	if level_over==1:
		game_text.no_levels()
	pygame.display.update()
	clock.tick(fps)