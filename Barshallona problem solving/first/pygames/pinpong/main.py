#the goal is to create a ping pong game 
import pygame
import decimal
import random
import keyboard
import math 
from pygame.locals import *
from array import *
pygame.init()
width ,hight = 700, 700
screen = pygame.display.set_mode((width, hight))
ball = pygame.image.load("resources/pall.png")
player1 = pygame.image.load("resources/player.png")
enemy = pygame.image.load("resources/player.png")
#ball info
ballpos = [200, 200]
ballsize = 40
anglex, angley, speed = 1.0, 0.45, 4.0
angles = [45, 60, 20, 50, 70, 30]
#player1 info 
player1position = [650, 350]
playerspeed = 2
playerdirection = [False, False]

#enemy info 
enemyposition = [50, 350]
enemyspeed = 6

#genral 
game = True

#cubes 

def collision(x1, y1,xlength, ylength, x2, xlength2, ylength2,  y2):
    output = False
    if x1 + xlength >= x2 and y1 + ylength >= y2 and y1<= y2 + ylength2 and x1 <= x2 + xlength2:
        output = True
        anglex = angles[random.randrange(0,6)]
    # elif  x2 + xlength2 >= x1 + xlength and y2 + ylength2 >= y1 + ylength:
    #     output = True
    return output

while game:
    screen.fill(0)
    screen.blit(ball, ballpos)
    screen.blit(player1, player1position)
    screen.blit(enemy, enemyposition)
    pygame.display.flip()

    #ball code 
    ballpos[0] += anglex * speed
    ballpos[1] += angley * speed
    angley += random.randrange(-1,1) * 0.1 
    #walls collision 
    if ballpos[0] <= 0 or ballpos[0] >= width - ballsize:
        anglex *= -1
    if ballpos[1] <= 0 or ballpos[1] >= hight - ballsize:
        angley *= -1
    #player one movement
    if playerdirection[0] == True:
        player1position[1] += 5 * playerspeed
    if playerdirection[1] == True:
        player1position[1] -= 5 * playerspeed
    
    #check for player and collide
    if collision(ballpos[0], ballpos[1],ballsize, ballsize,player1position[0], 30,150, player1position[1] ):
        anglex *= -1

    #enemy movment 
    distance = 1
    distance = ballpos[1] - enemyposition[1]
    distance /= 50
    enemyposition[1] += distance * enemyspeed
    #check enemy collider with enemy
    if collision(ballpos[0], ballpos[1],ballsize, ballsize,enemyposition[0], 20,150, enemyposition[1] ):
        anglex *= -1
    #win and lose functions 
    if ballpos[0] >= width - ballsize or ballpos[0] <= 1:
        game = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_s:
                playerdirection[0] = True
            if event.key == K_w:
                playerdirection[1] = True
        if event.type == pygame.KEYUP:
            if event.key == K_s:
                playerdirection[0] = False
            if event.key == K_w:
                playerdirection[1] = False
