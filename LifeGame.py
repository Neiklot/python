# pip install pygame

import pygame
import numpy as np
import time

# initializing the PyGame
pygame.init()

# Creating the world
width,height=500,500
screen = pygame.display.set_mode((500, 500))

# Colors of the world
BLACK_COLOUR = 25, 25, 25
screen.fill(BLACK_COLOUR)

# Number of cells
xCells, yCells = 25, 25

dimensionX = width/xCells
dimensionY = height/yCells

gameState = np.zeros((xCells, yCells))

# A Blinker model
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1


# Boocle for creating and to give life to the world
running = True
while running:

    # First we need to store the current status of the world
    newGameState = np.copy(gameState)
    # We should to clean
    screen.fill(bg)
    # We sould get the system a breath
    time.sleep(0.1)

    # Our way to scape from the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Our interaction as Gods
    mouseClick = pygame.mouse.get_pressed()
    if sum(mouseClick) > 0:
        posX, posY = pygame.mouse.get_pos()
        x, y = int(np.floor(posX/dimensionX)), int(np.floor(posY/dimensionY))
        newGameState[x, y] = not mouseClick[2]

    # Our controll for every zone in our world 
    for y in range(0, nxC):
        for x in range(0, nyC):

            # Your neighborhood affects you
            n_neigh = \
                gameState[(x-1) % xCells, (y-1) % nyC] + \
                gameState[(x) % xCells, (y-1) % yCells] + \
                gameState[(x+1) % xCells, (y-1) % yCells] + \
                gameState[(x-1) % xCells, (y) % yCells] + \
                gameState[(x+1) % xCells, (y) % yCells] + \
                gameState[(x-1) % xCells, (y+1) % yCells] + \
                gameState[(x) % xCells, (y+1) % yCells] + \
                gameState[(x+1) % xCells, (y+1) % yCells]


            # The physics that control all the world
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            # Fiat Lux
            poly = [((x)*dimCW, y*dimCH),
                    ((x+1)*dimCW, y*dimCH),
                    ((x+1)*dimCW, (y+1)*dimCH),
                    ((x)*dimCW, (y+1)*dimCH)]

            # Morituri te salutant
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # We update the world
    gameState = np.copy(newGameState)
    # We sould get the system a breath
    time.sleep(0.1)

    # the eye that sees everything
    pygame.display.flip()
