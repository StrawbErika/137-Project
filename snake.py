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

# def s
snakeHead = [250,250] 
snakeBody = [snakeHead,[240,250],[230,250]] 
apple = [random.randrange(1,40)*10,random.randrange(1,40)*10]

def showSnake(snakeBody):
    for position in snakeBody:
        pygame.draw.rect(display,red,pygame.Rect(position[0],position[1],10,10))
 
def showApple(display,apple):
    pygame.draw.rect(display,black,pygame.Rect(apple[0], apple[1],10,10))

def crashWithWall(snakeHead):
    if snakeHead[0]>=width or snakeHead[0]<=0 or snakeHead[1]>=height or snakeHead[1]<=0 :
        return 1
    else:
        return 0
def eatApple(snakeHead, apple):
    if snakeHead == apple:
        snake_position.insert(0,list(snake_head))
        score = score + 1

def snakeLogic(snakeHead, snakeBody, button):
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


def playGame(snakeHead, snakeBody, apple, button):
    crashed = False
    prevButton = 1
    button = 1
    currentVector = np.array(snakeBody[0])-np.array(snakeBody[1])

    while crashed is not True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crashed = True
            if crashWithWall(snakeHead):
                crashed = True
                print("GAME OVER")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and prevButton != 1:
                    button = 0
                elif event.key == pygame.K_RIGHT and prevButton != 0:
                    button = 1
                elif event.key == pygame.K_UP and prevButton != 2:
                    button = 3
                elif event.key == pygame.K_DOWN and prevButton != 3:
                    button = 2
                else:
                    button = button
        
        display.fill(windowColor)
        showSnake(snakeBody)
        showApple(display,apple)

        snakeBody= snakeLogic(snakeHead, snakeBody, button)
        pygame.display.update()
        prevButton = button
        clock = pygame.time.Clock()

        clock.tick(7)

playGame(snakeHead, snakeBody, apple, 1)
clock = pygame.time.Clock()
clock.tick(100)

pygame.quit()