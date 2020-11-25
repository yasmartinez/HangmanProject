#import random
#from WordList import wordList

import pygame

#game setup
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

#variables used for the buttons
radius = 20
gapSize = 15
#list for the buttons used
letters = []
startX = round((WIDTH - (radius * 2 + gapSize) * 13) / 2)
startY = 400

for i in range(26):
    x = startX + gapSize * 2 + ((radius * 2 + gapSize) * (i % 13))
    y =

#hangman pictures used
images = []
#loop cycles through the images for each point in hangman based on pic name
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#stage in where the hangman is
hangmanLife = 0


FPS = 60
clock = pygame.time.Clock()
run = True


while run:
    clock.tick(FPS)

    #background color
    win.fill((153, 179, 255))
    win.blit(images[hangmanLife], (100, 100))
    pygame.display.update()
    
    #this event is used to close the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    #taking in position of the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

pygame.quit
