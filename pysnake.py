import pygame 
import sys

WIDTH = 720
HEIGHT = 720
BLOCKSIZE = int(720/24)

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()

def main():
    grid = [[0 for i in range(24)] for j in range(24)]

    #0 = empty, 1 = snake, 2 = apple
    grid[4][12] = 1 #starting square
    grid[16][12] = 2 # first apple

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        i = 0
        for x in range(0,WIDTH,BLOCKSIZE):
            j = 0
            for y in range(0,HEIGHT,BLOCKSIZE):
                block = pygame.Rect(x,y,BLOCKSIZE,BLOCKSIZE)
                pygame.draw.rect(screen,blockColour(grid,i,j),block)
                j += 1
            i += 1         

        pygame.display.update()
        clock.tick(30) 


def blockColour(grid,i,j):
    if grid[i][j] == 0:
        return (0,0,0)
    elif grid[i][j] == 1:
        return (0, 150, 255)
    else:
        return (238, 75, 43)
               
main()