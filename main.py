#This code is just to create a 2d interface and a "character" if you go with the arrow keys to the edges you "die" and start over or quit the game

import pygame
import time

x = pygame.init()


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameOver_message = "End of the game, R to restart over or Q for to left the game"

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('TEST')

clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)

def message_to_screen(msg,color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [display_width/4, display_height/2])

def titleLoop():
	gamePlay = False
	gameExit = False
	lead_x = display_width/2
	lead_y = 2*display_height/3
	lead_x_change = 0

	while not gameExit:

		while gamePlay == False:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						lead_x_change = -10
					if event.key == pygame.K_RIGHT:
						lead_x_change = 10

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						lead_x_change = 0
				if lead_x >= 100:
					gamePlay = True
				elif lead_x <= 400:
					gameExit = True
		gameDisplay.fill(black)
		gameDisplay.fill(red, rect=[300, 400, 80, 40])
		gameDisplay.fill(red, rect=[100, 400, 80, 40])
		message_to_screen('TEST', white)
		pygame.display.update()
time.sleep(10)

def gameLoop():
	gameExit = False
	gameOver = False
	lead_x = display_width/2
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0

	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(white)
			message_to_screen(gameOver_message, red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
						gameExit = True
						gameOver = False
					if event.key == pygame.K_r:
						gameLoop()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					lead_y_change = 0

		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
			gameOver = True

		lead_x += lead_x_change
		lead_y += lead_y_change



		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block_size,block_size])
		pygame.display.update()

		clock.tick(FPS)

	pygame.quit()
	quit()

gameLoop()
