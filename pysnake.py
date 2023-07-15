import pygame 
import sys
import random

#window and block sizes
WIDTH = 720
HEIGHT = 720
BLOCKSIZE = int(720/24)

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()

class Snake():
    def __init__(self):
        self.x = 4
        self.y = 12
        self.veloY = 0
        self.veloX = 0
        self.length = 1
        self.occupies = [(4,12)]

    def update(self, keyEvent, grow,apple):
        #kills snake if it hits a wall
        if (self.x>24 or self.x < 0 or self.y > 24 or self.y < 0 or (self.x,self.y) in self.occupies):
            self.gameOver()
            apple.gameOver()
        #makes snake grow if it eats an apple and makes it look like its moving
        self.occupies.append((self.x,self.y,1 if keyEvent else 0))
        self.x += self.veloX
        self.y += self.veloY
        if not grow:
            self.occupies.pop(0)
        self.length += 1 if grow else self.length

    #resets the snake
    def gameOver(self):
        self.x = 4
        self.y = 12
        self.veloY = 0
        self.veloX = 0
        self.length = 1
        self.occupies = [(4,12)]


class Apple():
    def __init__(self):
        self.x = 16
        self.y = 12
    
    def update(self, grid):
        #places the apple on a new square if it is eaten
        self.newX, self.newY = random.randint(0,22), random.randint(0,22)
        while grid[self.newX][self.newY] != 0:
            self.newX, self.newY = random.randint(0,22), random.randint(0,22)
        self.x = self.newX
        self.y = self.newY
    
    def gameOver(self):
        self.x = 16
        self.y = 12



def main():

    snake = Snake()
    apple = Apple()

    while True:

        grid = [[0 for i in range(24)] for j in range(24)]
        keyEvent = False
        grow = False

        #0 = empty, 1 = snake, 2 = apple
        for point in snake.occupies:
            grid[point[0]][point[1]] = 1
        grid[apple.x][apple.y] = 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and snake.veloX == 0:
                    snake.veloX = -1
                    snake.veloY = 0
                    keyEvent = True
                elif event.key == pygame.K_d and snake.veloX == 0:
                    snake.veloX = 1
                    snake.veloY = 0
                    keyEvent = True
                elif event.key == pygame.K_w and snake.veloY == 0:
                    snake.veloY = -1
                    snake.veloX = 0
                    keyEvent = True
                elif event.key == pygame.K_s and snake.veloY == 0:
                    snake.veloY = 1
                    snake.veloX = 0
                    keyEvent = True

        i = 0
        for x in range(0,WIDTH,BLOCKSIZE):
            j = 0
            for y in range(0,HEIGHT,BLOCKSIZE):
                block = pygame.Rect(x,y,BLOCKSIZE,BLOCKSIZE)
               # if x == 0:
                #    pygame.draw.rect(screen,(255,255,255),block)
                #else:
                pygame.draw.rect(screen,blockColour(grid,i,j),block)
                j += 1
            i += 1

        if snake.x == apple.x and snake.y == apple.y:
            grow = True
            snake.update(keyEvent,grow,apple)
            apple.update(grid)
        else:
            snake.update(keyEvent,grow,apple)
        
        pygame.display.update()
        clock.tick(15) 

#gives blocks their colours
def blockColour(grid,i,j):
    if grid[i][j] == 0:
        return (0,0,0)
    elif grid[i][j] == 1:
        return (0, 150, 255)
    else:
        return (238, 75, 43)
               
main()