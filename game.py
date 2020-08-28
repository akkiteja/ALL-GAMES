# 1 import library
import pygame
import math
import random
from pygame.locals import *

# 2 initialize the game
movecount=5
arrowspeed=10
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[100, 100]
acc=[0,0] # players accuracy
arrows=[] # keep track of arrows -- [rotation, x, y]
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

# 3 Load images
player = pygame.image.load('resources/images/dude.png')
grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')
arrow = pygame.image.load('resources/images/bullet.png')
badguyimg1 = pygame.image.load('resources/images/badguy.png')
badguyimg = badguyimg1
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")

# 4 keep looping through
while 1:
	badtimer-=1

	# 5 clear screen before drawing it aain
	screen.fill(0)

	# 6 draw screen elements

	for x in range(width/grass.get_width() + 1):
		for y in range(height/grass.get_height() +1):
			screen.blit(grass, (x*100, y*100))

	screen.blit(castle, (0, 30))
	screen.blit(castle, (0, 135))
	screen.blit(castle, (0, 240))
	screen.blit(castle, (0, 345))

	# 6.1
	# atan2( diff x, diff y) = z
	# z is in radian
	position = pygame.mouse.get_pos() # get mouse x,y coordinate position
	angle = math.atan2(position[1] - (playerpos[1]+32), position[0] - (playerpos[0] + 26)) # 32 and 26 are width and height of the player icon
	playerrot = pygame.transform.rotate( player, 360 - angle*57.29)
	playerpos1 = (playerpos[0] - playerrot.get_rect().width/2, playerpos[1] - playerrot.get_rect().height/2)
	screen.blit( playerrot, playerpos1 )

	# 6.2
	for bullet in arrows:
		index=0
		velx=math.cos(bullet[0])*arrowspeed
		vely=math.sin(bullet[0])*arrowspeed
		bullet[1]+=velx
		bullet[2]+=vely

		if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
			arrows.pop(index)
		index += 1

		for projectile in arrows:
			arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
			screen.blit(arrow1, (projectile[1], projectile[2]))

	# 6.3
	if badtimer==0:
		badguys.append( [ 640, random.randint(50, 430)] )
		badtimer=100-(badtimer1*2)

		if badtimer1 >= 35:
			badtimer1=32
		else:
			badtimer1+=5
	index=0

	for badguy in badguys:
		if badguy[0]<-64:
			badguys.pop(index)
		badguy[0]-=7

		# 6.3.1 - Attack castle
		badrect = pygame.Rect(badguyimg.get_rect())
		badrect.top = badguy[1]
		badrect.left = badguy[0]
		if badrect.left < 64:
			healthvalue -= random.randint(5, 20)
			badguys.pop(index)
		
		# 6.3.2 Check for collision
		index1 = 0
		for bullet in arrows:
			bullrect = pygame.Rect(arrow.get_rect())			
			bullrect.left = bullet[1]
			bullrect.top = bullet[2]

			if badrect.colliderect(bullrect):
				acc[0] += 1
				badguys.pop(index)
				arrows.pop(index1)
			index1 += 1
		index+=1

	for badguy in badguys:
		screen.blit(badguyimg, badguy)

	# 6.4 Draw clock
	font = pygame.font.Font(None, 24)
	survivedtext = font.render( str(( 90000 - pygame.time.get_ticks())/60000) + ":" + str ((90000 - pygame.time.get_ticks()) / 1000 % 60).zfill(2), True, (0,0,0))
	textRect = survivedtext.get_rect()
	textRect.topright = [635, 5]
	screen.blit(survivedtext, textRect)

	# 6.5 Draw health bar
	screen.blit(healthbar, (5,5))
	for health1 in range(healthvalue):
		screen.blit( health, (health1+8, 8))

	# 7 update screen
	pygame.display.flip()

	# 8 loop through the events
	for event in pygame.event.get():
		# check if the event is the X button
		if event.type==pygame.QUIT:
			pygame.guit()
			exit(0)

		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys[0]=True
			elif event.key==K_a:
				keys[1]=True
			elif event.key==K_s:
				keys[2]=True
			elif event.key==K_d:
				keys[3]=True
		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0]=False
			elif event.key==K_a:
				keys[1]=False
			elif event.key==K_s:
				keys[2]=False
			elif event.key==K_d:
				keys[3]=False

		if event.type==pygame.MOUSEBUTTONDOWN:
			position=pygame.mouse.get_pos()
			acc[1]+=1
			arrows
			arrows.append([math.atan2(position[1] - (playerpos1[1]+32), position[0] - (playerpos1[0]+26)), playerpos1[0]+32, playerpos1[1]+32])


	# 9 move player
	if keys[0]:
		playerpos[1] -= movecount
	elif keys[2]:
		playerpos[1] += movecount 
	if keys[1]:
		playerpos[0] -= movecount
	elif keys[3]:
		playerpos[0] += movecount


