from math import pi
import pygame
import numpy as np
import time
import random

pygame.init()

width = 500 
height = 500    
display = pygame.display.set_mode((width,height))
windowColor= (200,200,200)
display.fill(windowColor)
pygame.display.update()

red = (255,0,0)  
black = (0,0,0)

def showSnake(snakeBody):
    for position in snakeBody:
        pygame.draw.rect(display,red,pygame.Rect(position[0],position[1],10,10))
 
def showApple(display,apple):
    pygame.draw.rect(display,black,pygame.Rect(apple[0], apple[1],10,10))

def crashedWithWall(snakeHead):
    if snakeHead[0]>=width or snakeHead[0]<=0 or snakeHead[1]>=height or snakeHead[1]<=0 :
        return 1
    else:
        return 0

def eatApple(snakeHead,snakeBody, apple):
    snakeBody.insert(0,list(snakeHead))
    # score = score + 1
    apple = [random.randrange(1,40)*10,random.randrange(1,40)*10]
    return apple

def moveSnake(snakeHead, snakeBody, button):
    if button == 1:
        snakeHead[0] += 10
    elif button == 0:
        snakeHead[0] -= 10
    elif button == 2:
        snakeHead[1] += 10
    elif button == 3:
        snakeHead[1] -= 10
    else:
        pass
    snakeBody.insert(0,list(snakeHead))
    snakeBody.pop()
    
    return snakeBody

def spawnApple():
    apple = [random.randrange(1,40)*10,random.randrange(1,40)*10]
    return apple

def spawnSnake():
    xSnake = random.randrange(1,40)*10
    ySnake = random.randrange(1,40)*10
    snakeHead = [xSnake,ySnake]
    snakeBody = [[xSnake,ySnake],[xSnake-10,ySnake],[xSnake-10,ySnake]] 
    return snakeHead, snakeBody

def crashedWithSelf(snakeHead, snakeBody):
    snakeHead = snakeBody[0]
    if snakeHead in snakeBody[1:]:
        return 1
    else:
        return 0

def snakePlay(crashed, apple, button):
    snakeHead,snakeBody = spawnSnake()
    currentVector = np.array(snakeBody[0])-np.array(snakeBody[1])
    while crashed is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and prevButton != 1:
                    button = 0
                elif event.key == pygame.K_RIGHT and prevButton != 0:
                    button = 1
                elif event.key == pygame.K_DOWN and prevButton != 3:
                    button = 2
                elif event.key == pygame.K_UP and prevButton != 2:
                    button = 3
                else:
                    button = button

        if crashedWithWall(snakeHead):
            crashed = True
        if crashedWithSelf(snakeHead, snakeBody):
            crashed = True
        if snakeHead == apple:
            apple = eatApple(snakeHead,snakeBody,apple)

        display.fill(windowColor)
        showSnake(snakeBody)
        showApple(display,apple)
        snakeBody= moveSnake(snakeHead, snakeBody, button)
        prevButton = button
        clock = pygame.time.Clock()
        clock.tick(7)
        pygame.display.update()


def playGame():
    apple = spawnApple()    
    crashed = False
    prevButton = 1
    button = 1
    snakePlay(crashed, apple, button)
    snakePlay(crashed, apple, button)

playGame()
clock = pygame.time.Clock()
clock.tick(100)

pygame.quit()