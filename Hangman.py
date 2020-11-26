#import random
#from WordList import wordList
import math
import pygame

#game setup
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

#variables used for the buttons
radius = 20
gapSize = 15

#colors
black = (0, 0, 0)
lightBlue = (153, 179, 255)
#list for the buttons used
letters = [] 
startX = round((WIDTH - (radius * 2 + gapSize) * 13) / 2)
startY = 400
#ascii letter value for capital A
A = 65
#loop used to maintain the buttons on the screen into rows
for i in range(26):
    #used to gather the two letter rows
    x = startX + gapSize * 2 + ((radius * 2 + gapSize) * (i % 13))
    y = startY + ((i // 13) * (gapSize + radius * 2))
    letters.append([x,y, chr(A + i), True])

#font used for game
lettersFont = pygame.font.SysFont('Helvetica', 30)

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

def drawings():
    #background color
    win.fill((lightBlue))

    #button colors
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, black, (x, y), radius, 3)
            text = lettersFont.render(ltr, 1, black)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        
    #location of hangman image
    win.blit(images[hangmanLife], (100, 100))
    pygame.display.update()

while run:
    clock.tick(FPS)

    drawings()
    
    #this event is used to close the application
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    #taking in position of the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            #tracking mouse input for the button clicks
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                #distance between mouse positions
                    distance = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    #removal of the button after selection
                    if distance < radius:
                        letter[3] = False
                        [3, 4, "A", False]

pygame.quit
