import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([500, 500])
screen_rect = screen.get_rect()

platform = pygame.image.load("00_images\land.png")
platform_rect = platform.get_rect()
platform = pygame.transform.scale(platform, (2*screen_rect.width,platform_rect.height))
platform_rect = platform.get_rect()
# platform_rect.x, platform_rect.y = 250-platform_rect.width/2, 500-platform_rect.height
platform_rect.midbottom = screen_rect.midbottom

def platform_move():
    platform_rect.x -= 5
    if platform_rect.centerx == 0:
        platform_rect.left = screen_rect.left


    

bird = pygame.image.load("00_images/bird.png")
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center

upper_pipe = pygame.Rect(0 , 0 , 0.15*screen_rect.width , 0.4*screen_rect.height)
upper_pipe.topright = screen_rect.topright

bottom_pipe = pygame.Rect(0 , 0 , 0.15*screen_rect.width , 0.4*screen_rect.height)
bottom_pipe.bottomright = screen_rect.bottomright

upper_head_pipe = pygame.Rect(0 , 0 , 1.2*upper_pipe.width , 0.1*upper_pipe.height)
upper_head_pipe.midbottom = upper_pipe.midbottom

bottom_head_pipe = pygame.Rect(0 , 0 , 1.2*bottom_pipe.width , 0.1*bottom_pipe.height)
bottom_head_pipe.midtop = bottom_pipe.midtop

def upper_pipe_move():
    upper_pipe.x -= 5
    if upper_pipe.centerx == 0:
        upper_pipe.left = screen_rect.left

def bottom_pipe_move():
    bottom_pipe.x -= 5
    if bottom_pipe.centerx == 0:
        bottom_pipe.left = screen_rect.left

def upper_head_pipe_move():
    upper_head_pipe.x -= 5
    if upper_head_pipe.centerx == 0:
        upper_head_pipe.left = screen_rect.left

def bottom_head_pipe_move():
    bottom_head_pipe.x -= 5
    if bottom_head_pipe.centerx == 0:
        bottom_head_pipe.left = screen_rect.left
        
bird_fly = False
def bird_move:
    if bird_fly:
        print('Bird is flying')
    else

def event_listener():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
      
			if event.key == pygame.K_SPACE:
       
				bird_fly = True
    
		elif event.type == pygame.KEYUP:
      
			if event.key == pygame.K_SPACE:
       
				bird_fly = False
				


while True:
	pygame.display.flip() # draw - clear - draw dst.
	
	screen.fill([245, 66, 239]) #light purple
	pygame.draw.rect(screen , (60,60,60),upper_pipe)
	pygame.draw.rect(screen , (60,60,60),bottom_pipe)
	pygame.draw.rect(screen , (60,60,60),upper_head_pipe)
	pygame.draw.rect(screen , (60,60,60),bottom_head_pipe)
	screen.blit(platform, platform_rect)
	platform_move()
	upper_pipe_move()
	bottom_pipe_move()
	upper_head_pipe_move()
	bottom_head_pipe_move()
	screen.blit(bird, bird_rect)
 


	pygame.time.Clock().tick(25) # 25 frames in a second
	event_listener()
 
	


