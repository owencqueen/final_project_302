### 3D User Interface for Cube ###

import pygame
import sys
import math

class Camera:

	def __init__(self, cam_pos = (0,0,0), cam_rot = (0,0) ):
		self.cam_pos = list(cam_pos)
		self.cam_rot = list(cam_rot)

	def event_handler(self, event):
		if event.type == pygame.MOUSEMOTION:
			x,y = event.rel
			x /= 200
			y /= 200
			self.rot[0] += x
			self.rot[1] += y

	def update(self, dt, key):
		mv = dt * 10
		
		# Raise and lower
		if key[pygame.K_q] : self.cam_pos[1] += mv
		if key[pygame.K_e] : self.cam_pos[1] -= mv
		
		# Movement
		if key[pygame.K_w] : self.cam_pos[2] += mv
		if key[pygame.K_s] : self.cam_pos[2] -= mv
		if key[pygame.K_a] : self.cam_pos[0] += mv
		if key[pygame.K_d] : self.cam_pos[0] -= mv


class Cube3d:
	def __init__(self):
		pass


def rotate2d(pos,rad):
	pass	

# Initialize window
pygame.init()
w,h = 720, 480		# Dimensions
cx, cy = w//2, h//2	# Cursor

screen = pygame.display.set_mode( (w, h) )
clock = pygame.time.Clock()

# Initialize camera
cam = Camera( (0,0,-5) )

while 1:
	# Update clocktime
	dt = clock.tick()/1000
	
	# Exit if closed
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()
	
	# White background
	screen.fill( (255, 255, 255) )

	# Update
	pygame.display.flip()


	key = pygame.key.get_pressed()
	cam.update(dt, key);

